from typing import NamedTuple

from django.core.management import call_command
from django.core.management import get_commands
from django.core.management.base import BaseCommand
from django.utils.translation import gettext_lazy as _

from .models import Category


class Command(BaseCommand):
    help = "Populate transaction categories"

    def handle(self, *args, **options):
        categories = [
            {"name": "Food", "description": "All food expenses"},
            {"name": "Transport", "description": "All transport expenses"},
            {"name": "Salary", "description": "All salary incomes"},
            {"name": "Rent", "description": "All rent expenses"},
            {"name": "Health", "description": "All health expenses"},
        ]
        for category in categories:
            category, _ = Category.objects.get_or_create(name=category["name"], description=category["description"])
