from django.core.management.base import BaseCommand
from django.conf import settings

from confidence import Configuration
from confidence.utils import print_formatted


class Command(BaseCommand):
    help = 'Deletes all confidence configuration files.'

    def handle(self, *args, **options):
        config = Configuration(settings.BASE_DIR)
        result = config.cleanup()

        if result:
            print_formatted(f'Deleted directory and all files in {config.workdir}.')
        else:
            print_formatted(f'Confidence working directory doesn\'t exist at {config.workdir}.')
