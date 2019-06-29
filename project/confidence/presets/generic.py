from . import Preset


class ProjectSettingsPreset(Preset):
    title = 'project'
    verbose_name = 'Project'

    options = {
        'name': None,
        'version': None,
        'site_url': None,
    }


class EnvironmentSettingsPreset(Preset):
    title = 'environment'
    verbose_name = 'Environment'

    options = {
        'secret_key': None,
        'debug': False,
        'allowed_hosts': [],
        'database': None,
        'cache': None,
        'mailing': None,
    }
