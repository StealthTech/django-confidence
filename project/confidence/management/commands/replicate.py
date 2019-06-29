import os

from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

from confidence import Configuration


class Command(BaseCommand):
    help = 'Creates project configuration file from blueprint.'

    def handle(self, *args, **options):
        config = Configuration(settings.BASE_DIR)
        config.replicate()
