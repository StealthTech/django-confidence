import os
import json

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
        self.workdir = os.path.join(workdir, '_confidence')

        self.settings_filepath = os.path.join(self.workdir, 'settings.json')
        self.blueprint_filepath = os.path.join(self.workdir, 'blueprint.json')

        self.settings = self.load_settings()
        self.blueprint = self.load_blueprint()

        filename = self.settings.get('filename')
        self.filepath = os.path.join(self.workdir, filename) if filename else None

        self.content = self.load()

    def __getitem__(self, item):
        return self.content[item]

    def __setitem__(self, key, value):
        self.content[key] = value

    def get(self, key, default=None):
        return self.content.get(key, default)

    def _prepare_workdir(self):
        return os.makedirs(self.workdir, exist_ok=True)

    def blueprint_exists(self):
        return os.path.exists(self.blueprint_filepath)

    def settings_exists(self):
        return os.path.exists(self.settings_filepath)

    def exists(self):
        return os.path.exists(self.filepath)

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

        with open(self.settings_filepath, 'w') as f:
            json.dump(settings_dct, f, indent=4)

    def initialize(self, presets_lst):
        self._prepare_workdir()

        config_dct = {
            preset.title: preset.options for preset in presets_lst
        }

        with open(self.blueprint_filepath, 'w') as f:
            json.dump(config_dct, f, indent=4)

    def set_filename(self, filename):
        self.filepath = os.path.join(self.workdir, filename)

    def replicate(self):
        with open(self.blueprint_filepath, 'r') as f:
            blueprint = json.load(f)

        with open(self.filepath, 'w') as f:
            json.dump(blueprint, f, indent=4)
