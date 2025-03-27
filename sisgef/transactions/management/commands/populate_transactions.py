from django.core.management.base import BaseCommand

from sisgef.transactions.tests.factories import ExpenseFactory
from sisgef.transactions.tests.factories import IncomeFactory


class Command(BaseCommand):
    help = "Populate the database with income and expense objects"

    def add_arguments(self, parser):
        parser.add_argument(
            "--incomes", type=int, default=10,
            help="Number of income objects to create",
        )
        parser.add_argument(
            "--expenses", type=int, default=10,
            help="Number of expense objects to create",
        )

    def handle(self, *args, **options):
        incomes_count = options["incomes"]
        expenses_count = options["expenses"]

        self.stdout.write(f"Creating {incomes_count} income objects...")
        IncomeFactory.create_batch(incomes_count)

        self.stdout.write(f"Creating {expenses_count} expense objects...")
        ExpenseFactory.create_batch(expenses_count)

        self.stdout.write(
            self.style.SUCCESS(
                "Database successfully populated with income and expense objects."))
