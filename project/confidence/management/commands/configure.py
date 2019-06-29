from django.core.management.base import BaseCommand
from django.conf import settings

from confidence import Configuration
from confidence.utils import print_formatted, input_formatted


class Command(BaseCommand):
    help = 'Creates project configuration blueprint and optionally configuration file.'

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

            filename = input_formatted(
                'Enter configuration file name (leave it blank for `config.json`): '
            ) or 'config.json'

            if not filename.endswith('.json'):
                filename += '.json'
            settings_dct['filename'] = filename

            environments = input_formatted(
                'Enter your root environment layouts separated by spaces'
                ' (leave it blank for `development production`): '
            ).split() or ['development', 'production']
            settings_dct['environments'] = environments

            config.setup(settings_dct)
            config.set_filename(filename)
        else:
            print_formatted(f'Found already set configuration file name: `{config.settings["filename"]}`.')

        if config.blueprint_exists() and not option_blank:
            response = input_formatted(f'Found blueprint at {config.blueprint_filepath}. Rewrite? Y/n ')
            if response.lower() not in ['y', 'yes']:
                print_formatted('Aborting operation.')
                return

        # Preset selection / Start
        print_formatted('Choose presets that you want to use in your configuration:')
        presets = []
        idx = 0
        for group in config.presets.values():
            print_formatted(f'- - - [{group["verbose_name"]}] - - -')

            for preset in group['items']:
                presets.append(preset)
                preset_name = preset.get_full_verbose_name()
                print_formatted(f'{idx + 1} : {preset_name}', level=1)
                idx += 1

        preset_idxs_spl = input_formatted('Enter indices of presets you\'ve chosen separated by spaces: ').split()

        selected_presets = []
        for preset_idx in preset_idxs_spl:
            try:
                idx = int(preset_idx) - 1
                selected_presets.append(presets[idx])
            except (IndexError, ValueError) as e:
                pass
        # Presets selection / End

        config.initialize(selected_presets)
        print_formatted(f'Created configuration blueprint at {config.blueprint_filepath}.')

        if option_apply:
            config.replicate()
            print_formatted(f'Created configuration file at {config.filepath}.')
