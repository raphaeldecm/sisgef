from typing import NamedTuple

from django.core.management import call_command
from django.core.management import get_commands
from django.core.management.base import BaseCommand


class CommandItem(NamedTuple):
    name: str
    initial_message: str


COMMANDS = [
    CommandItem("migrate", "Migrating database..."),
    CommandItem("update_user_profiles", "Updating user profiles..."),
    CommandItem("create_admin_user", "Creating superuser..."),
    CommandItem("populate_category", "Populating categories..."),
]


class Command(BaseCommand):
    help = "Load database"

    def handle(self, *args, **options):
        valid_commands = [
            command for command in COMMANDS if command.name in get_commands()
        ]
        for command in valid_commands:
            self.stdout.write(command.initial_message)
            call_command(command.name)
