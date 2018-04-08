import configparser
import os


class Configuration:
    @classmethod
    def compile_from_presets(cls, filepath, presets):
        markup = {}
        for preset in presets:
            markup.update(preset.markup)
        return cls(filepath, markup)

    def __init__(self, filepath, markup):
        self.filepath = filepath
        self.markup = markup

    def exists(self):
        return os.path.exists(self.filepath)

    def make(self, force=False):
        if self.exists() and not force:
            raise FileExistsError('File already exists.')

        directory, filename = os.path.split(self.filepath)
        if directory and not os.path.exists(directory):
            os.makedirs(directory)

        conf = configparser.ConfigParser()

        for section, option_dict in self.markup.items():
            conf[section] = {}
            for option, value_raw in option_dict.items():
                if value_raw is None:
                    value = ''
                elif isinstance(value_raw, list):
                    value = ', '.join([str(e) for e in value_raw])
                else:
                    value = str(value_raw)

                conf[section][option] = value

        with open(self.filepath, 'w') as f:
            conf.write(f)

    def get(self, section, option):
        config = configparser.ConfigParser()
        config.read(self.filepath)

        try:
            return config[section][option]
        except (configparser.NoSectionError, configparser.NoOptionError):
            return None

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
