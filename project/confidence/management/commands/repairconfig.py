from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

from confidence import Configuration


class Command(BaseCommand):
    help = 'Checks if project configuration file already exists.'

    def handle(self, *args, **options):
        project_conf_variable = 'PROJECT_CONF'
        if not hasattr(settings, project_conf_variable):
            CommandError('Seems like there\'s no {} variable specified in your settings.py. '
                         'You need to set it with a Configuration instance first '
                         'to use this management command.'.format(project_conf_variable))

        project_conf = getattr(settings, project_conf_variable)
        if not isinstance(project_conf, Configuration):
            CommandError('Variable {} in settings.py must be a Configuration instance.'.format(project_conf_variable))

        if not project_conf.exists():
            message = self.style.WARNING('[WARNING] Configuration file doesn\'t '
                                         'exist at {}.'.format(project_conf.filepath))
            self.stdout.write(message)
            project_conf.make()
        else:
            message = '[INFO] Configuration file found at {}'.format(project_conf.filepath)
            self.stdout.write(message)
            project_conf.repair()
