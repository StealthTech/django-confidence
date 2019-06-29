from django.core.management.base import BaseCommand
from django.conf import settings

from confidence import Configuration
from confidence.utils import print_formatted


class Command(BaseCommand):
    help = 'Creates project configuration file from blueprint.'

    def handle(self, *args, **options):
        config = Configuration(settings.BASE_DIR)
        result = config.replicate()

        if result:
            print_formatted(f'Created configuration file at {config.filepath} from blueprint.')
        else:
            print_formatted(f'Blueprint doesn\'t exist. You may need to run `python manage.py configure` first.')
