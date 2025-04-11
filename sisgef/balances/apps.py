import contextlib

from django.apps import AppConfig


class BalancesConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "sisgef.balances"
    verbose_name = "Balances"

    def ready(self):
        with contextlib.suppress(ImportError):
            import sisgef.balances.signals # type: ignore # noqa: F401

