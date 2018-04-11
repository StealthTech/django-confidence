from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

from confidence import Configuration


class Command(BaseCommand):
    help = 'Creates project configuration file.'

    def add_arguments(self, parser):
        parser.add_argument(
            '--force',
            action='store_true',
            dest='force',
            help='Force management command to rewrite configuration file with defaults if it already exists.',
        )

    def handle(self, *args, **options):
        project_conf_variable = 'PROJECT_CONF'
        if not hasattr(settings, project_conf_variable):
            CommandError('Seems like there\'s no {} variable specified in your settings.py. '
                         'You need to set it with a Configuration instance first '
                         'to use this management command.'.format(project_conf_variable))

        project_conf = getattr(settings, project_conf_variable)
        if not isinstance(project_conf, Configuration):
            CommandError('Variable {} in settings.py must be a Configuration instance.'.format(project_conf_variable))

        try:
            project_conf.make(force=options.get('force'))
        except (FileExistsError, OSError) as ex:
            message = self.style.ERROR('[ERROR] Can\'t create a configuration file at {}.'
                                       '\nREASON: {}'.format(project_conf.filepath, ex))
        else:
            message = self.style.SUCCESS('[SUCCESS] Created a configuration file at {}'.format(project_conf.filepath))

        self.stdout.write(message)
