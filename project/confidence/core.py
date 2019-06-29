import os
import json
import shutil

from .presets.generic import ProjectSettingsPreset, EnvironmentSettingsPreset
from .presets.databases import PostgreSQLPreset, MySQLPreset
from .presets.cache import RedisPreset
from .presets.mailing import MailDevPreset


class Configuration:
    presets = {
        'generic': {
            'verbose_name': 'Generic',
            'items': [
                ProjectSettingsPreset,
                EnvironmentSettingsPreset,
            ]
        },
        'databases': {
            'verbose_name': 'Databases',
            'items': [
                PostgreSQLPreset,
                MySQLPreset,
            ],
        },
        'cache': {
            'verbose_name': 'Cache',
            'items': [
                RedisPreset,
            ]
        },
        'mailing': {
            'verbose_name': 'Mailing',
            'items': [
                MailDevPreset,
            ],
        },
    }

    def __init__(self, workdir):
        self.workdir = os.path.join(workdir, '.confidence')

        self.settings_filepath = os.path.join(self.workdir, 'settings.json')
        self.blueprint_filepath = os.path.join(self.workdir, 'blueprint.json')

        self.settings = self.load_settings()
        self.blueprint = self.load_blueprint()

        filename = self.settings.get('filename')
        self.filepath = os.path.join(self.workdir, filename) if filename else None

        self.current_environment = os.environ.get('CONFIDENCE_ENV')

        self.content = self.load()

    def __getitem__(self, item):
        if self.is_current_environment_valid():
            return self.content[self.current_environment][item]
        return self.content[item]

    def __setitem__(self, key, value):
        if self.is_current_environment_valid():
            self.content[self.current_environment][key] = value
        else:
            self.content[key] = value

    def get_raw(self, key, default=None):
        if self.is_current_environment_valid():
            return self.content[self.current_environment].get(key, default)
        return self.content.get(key, default)

    def get(self, chain, default=None):
        keys = chain.split('.')

        if self.is_current_environment_valid():
            obj = self.content[self.current_environment]
        else:
            obj = self.content

        for key in keys:
            if obj is None:
                return default
            obj = obj.get(key)
        return obj

    def is_current_environment_valid(self):
        return self.current_environment in self.settings.get('environments', [])

    def _prepare_workdir(self):
        return os.makedirs(self.workdir, exist_ok=True)

    def blueprint_exists(self):
        return os.path.exists(self.blueprint_filepath)

    def settings_exists(self):
        return os.path.exists(self.settings_filepath)

    def exists(self):
        return os.path.exists(self.filepath) if self.filepath else False

    def load_settings(self):
        if not self.settings_exists():
            return dict()
        with open(self.settings_filepath, 'r') as f:
            result = json.load(f)
        return result

    def load_blueprint(self):
        if not self.blueprint_exists():
            return dict()
        with open(self.blueprint_filepath, 'r') as f:
            result = json.load(f)
        return result

    def load(self):
        if not self.exists():
            return dict()
        with open(self.filepath, 'r') as f:
            result = json.load(f)
        return result

    def setup(self, settings_dct):
        self._prepare_workdir()
        self.settings = settings_dct

        with open(self.settings_filepath, 'w') as f:
            json.dump(settings_dct, f, indent=4)

    def initialize(self, presets_lst, extra_layout=None):
        self._prepare_workdir()
        environment_lst = self.settings['environments']

        environment_dct = {
            preset.title: preset.options for preset in presets_lst
        }

        config_dct = {
            environment: environment_dct for environment in environment_lst
        }

        if extra_layout:
            config_dct.update(extra_layout)

        with open(self.blueprint_filepath, 'w') as f:
            json.dump(config_dct, f, indent=4)

    def set_filename(self, filename):
        self.filepath = os.path.join(self.workdir, filename)

    def replicate(self):
        try:
            with open(self.blueprint_filepath, 'r') as f:
                blueprint = json.load(f)
        except FileNotFoundError:
            return False

        with open(self.filepath, 'w') as f:
            json.dump(blueprint, f, indent=4)
        return True

    def cleanup(self):
        try:
            shutil.rmtree(self.workdir)
            return True
        except FileNotFoundError:
            return False
