import contextlib

from django.apps import AppConfig


class TransactionsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "sisgef.transactions"
    verbose_name = "Transactions"

    def ready(self):
        with contextlib.suppress(ImportError):
            import sisgef.transactions.signals  # type: ignore # noqa: F401

