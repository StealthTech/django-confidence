import os

from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

from confidence import Configuration


class Command(BaseCommand):
    help = 'Creates project configuration file.'

    def add_arguments(self, parser):
        parser.add_argument(
            '--apply',
            action='store_true',
            dest='apply',
            help='Force management command to create configuration file from blueprint.',
        )
        parser.add_argument(
            '--blank',
            action='store_true',
            dest='blank',
            help='Force management command to rewrite configuration file if it already exists.',
        )

    def handle(self, *args, **options):
        option_apply = options.get('apply')
        option_blank = options.get('blank')

        config = Configuration(settings.BASE_DIR)

        if not config.settings or option_blank:
            settings_dct = dict()

            filename = input('Введите название для конфигурационного файла (по-умолчанию config.json): ') or 'config.json'
            if not filename.endswith('.json'):
                filename += '.json'
            settings_dct['filename'] = filename

            config.setup(settings_dct)
            config.set_filename(filename)
        else:
            print(f'Найдено ранее указанное имя конфигурационного файла: {config.settings["filename"]}')

        if config.blueprint_exists() and not option_blank:
            response = input(f'Обнаружен blueprint по пути {config.blueprint_filepath}. Перезаписать? Y/n ')
            if response.lower() not in ['y', 'yes']:
                print('Отмена операции.')
                return

        # Выбор пресетов из списка / Начало
        print('Для настройки доступны следующие пресеты:')
        presets = []
        idx = 0
        for _, group in config.presets.items():
            print(f'- - [{group["verbose_name"]}] - -')

            for preset in group['items']:
                presets.append(preset)
                preset_name = preset.get_full_verbose_name()
                print(f'{idx + 1} : {preset_name}')
                idx += 1

        preset_idxs_spl = input('Введите номера выбранных пресетов через пробел: ').split()

        selected_presets = []
        for preset_idx in preset_idxs_spl:
            try:
                idx = int(preset_idx) - 1
                selected_presets.append(presets[idx])
            except (IndexError, ValueError) as e:
                pass

        # Выбор пресетов из списка / Конец

        config.initialize(selected_presets)
        print(f'Шаблон конфигурационного файла создан по пути {config.blueprint_filepath}')

        if option_apply:
            config.replicate()
            print(f'Конфигурационный файл создан по пути {config.filepath}')
