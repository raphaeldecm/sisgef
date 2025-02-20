import json

from django.conf import settings
from django.core.management.base import BaseCommand

from sisgef.transactions.models import Category

CATEGORIES_JSON = str(settings.APPS_DIR / "transactions" / "bin" / "categories.json")

class Command(BaseCommand):
    help = "Populate transaction categories"

    def handle(self, *args, **options):
        with open(CATEGORIES_JSON, "r", encoding="utf-8") as json_data:
            categories = json.load(json_data)
            for category in categories:
                Category.objects.get_or_create(
                    name=category["name"],
                    description=category["description"],
                    category_type=category["category_type"],
                )
        self.stdout.write("Categories were updated successfully")
