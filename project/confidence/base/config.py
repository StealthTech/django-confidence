import configparser
import os


class Configuration:
    @classmethod
    def compile_from_presets(cls, filepath, presets, instant_start=False):
        markup = {}
        for preset in presets:
            markup.update(preset.markup)
        return cls(filepath, markup, instant_start)

    def __init__(self, filepath, markup, instant_start=False):
        self.filepath = filepath
        self.markup = markup
        self.instant_start = instant_start

        if not self.exists():
            self.make()

    def exists(self):
        return os.path.exists(self.filepath)

    @staticmethod
    def value_to_str(value):
        # TODO: JSON Encoding
        if value is None:
            result = ''
        elif isinstance(value, list):
            result = ', '.join([str(e) for e in value])
        else:
            result = str(value)
        return result

    @staticmethod
    def str_to_value(value):
        # TODO: JSON Decoding
        return value

    def make(self, force=False):
        if self.exists() and not force:
            raise FileExistsError('File already exists.')

        directory, filename = os.path.split(self.filepath)
        if directory and not os.path.exists(directory):
            os.makedirs(directory)

        config = configparser.ConfigParser()

        for section, option_dict in self.markup.items():
            config[section] = {}
            for option, value in option_dict.items():
                config[section][option] = self.value_to_str(value)

        with open(self.filepath, 'w') as file:
            config.write(file)

        if not self.instant_start:
            print('Configuration file created at {}. You may want to edit it before application start.'.format(self.filepath))
            exit()

    def repair(self):
        config = configparser.ConfigParser()
        config.read(self.filepath)

        sections_existing = config.sections()
        sections_declared = self.markup.keys()

        sections_missing = list(set(sections_declared) - set(sections_existing))
        if sections_missing:
            print('[WARNING] Missing sections (marked for repair): {}.'.format(', '.join(sections_missing)))

        sections_extra = list(set(sections_existing) - set(sections_declared))
        if sections_extra:
            print('[WARNING] Extra sections (ignoring): {}.'.format(', '.join(sections_extra)))

        sections_declared_existing = list(set(sections_existing).intersection(sections_declared))

        for section in sections_declared_existing:
            option_dict = self.markup.get(section)
            for option, value in option_dict.items():
                try:
                    config.get(section, option)
                except configparser.NoOptionError:
                    config[section][option] = self.value_to_str(value)
                    print('[WARNING] Missing [{}] option in [{}] section (repaired).'.format(option, section))

        for section in sections_missing:
            config[section] = {option: self.value_to_str(value) for option, value in self.markup[section].items()}
            print('[INFO] Added [{}] section.'.format(section))

        with open(self.filepath, 'w') as file:
            config.write(file)

        print('[INFO] Successfully repaired configuration file.')

    def get(self, section, option):
        config = configparser.ConfigParser()
        config.read(self.filepath)

        try:
            return config.get(section, option)
        except (configparser.NoSectionError, configparser.NoOptionError):
            markup_options = self.markup.get(section)

            if not markup_options:
                return

            markup_value = markup_options.get(option)
            return markup_value

    def get_bool(self, section, option):
        value = self.get(section, option)
        value_map = {'True': True, 'False': False}

        result = value_map.get(value)
        if result:
            return result
        return bool(result)

    def get_csv(self, section, option):
        value = self.get(section, option)
        return value.replace(' ', '').split(',')

    def get_int(self, section, option):
        value = self.get(section, option)
        return int(value)

    def get_float(self, section, option):
        value = self.get(section, option)
        return float(value)
