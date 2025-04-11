from django.db import models

from sisgef.core.models import BaseModel


class Balance(BaseModel):
    month = models.PositiveIntegerField(
        verbose_name="Mês", choices=[(i, i) for i in range(1, 13)],
    )
    year = models.PositiveIntegerField(verbose_name="Ano")
    total_income = models.DecimalField(
        verbose_name="Total de Receitas", max_digits=10, decimal_places=2, default=0,
    )
    total_expense = models.DecimalField(
        verbose_name="Total de Despesas", max_digits=10, decimal_places=2, default=0,
    )
    balance = models.DecimalField(
        verbose_name="Saldo Final", max_digits=10, decimal_places=2, default=0,
    )

    class Meta:
        unique_together = ("month", "year")
        verbose_name = "Saldo Mensal"
        verbose_name_plural = "Saldos Mensais"

    def calculate_balance(self):
        self.balance = self.total_income - self.total_expense
        self.save()

    def is_positive(self):
        return self.balance >= 0

    def __str__(self):
        status = "Positivo" if self.is_positive() else "Negativo"
        return f"Saldo de {self.month}/{self.year}: {self.balance} ({status})"
