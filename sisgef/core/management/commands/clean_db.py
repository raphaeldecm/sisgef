from django.conf import settings
from django.core.management import call_command
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Clean database with "migrate zero"'

    def handle(self, *args, **options):
        app_names = [name.split(".")[-1] for name in settings.LOCAL_APPS]
        for app_name in app_names:
            call_command("migrate", app_name, "zero")
