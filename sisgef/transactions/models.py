from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

from sisgef.balances.models import Balance
from sisgef.core.constants import MAX_CHAR_FIELD_NAME_LENGTH
from sisgef.core.models import BaseModel

User = get_user_model()


class Category(BaseModel):
    class Type(models.TextChoices):
        INCOME = "IN", _("Receita")
        EXPENSE = "EX", _("Despesa")

    name = models.CharField(max_length=MAX_CHAR_FIELD_NAME_LENGTH)
    description = models.TextField()
    type = models.CharField(max_length=2, choices=Type.choices)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self) -> str:
        return self.name


class Transaction(BaseModel):
    class PaymentMethod(models.TextChoices):
        CASH = "CA", _("Dinheiro")
        CREDIT_CARD = "CC", _("Cartão de Crédito")
        DEBIT_CARD = "DC", _("Cartão de Débito")
        PIX = "PX", _("PIX")
        TRANSFER = "TR", _("Transferência Bancária")
        BOLETO = "BL", _("Boleto Bancário")
        CHEQUE = "CH", _("Cheque")
        OTHER = "OT", _("Outro")

    class PaymentStatus(models.TextChoices):
        PENDING = "PD", _("Pendente")
        PAID = "PA", _("Pago")
        CANCELED = "CA", _("Cancelado")
        OVERDUE = "OV", _("Atrasado")

    class Frequency(models.TextChoices):
        DAILY = "DA", _("Diário")
        WEEKLY = "WE", _("Semanal")
        MONTHLY = "MO", _("Mensal")

    status = models.CharField(max_length=10, choices=PaymentStatus.choices)
    description = models.TextField(verbose_name="Descrição")
    value = models.DecimalField(verbose_name="Valor", max_digits=6, decimal_places=2)
    date = models.DateTimeField()
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    payment_method = models.CharField(max_length=2, choices=PaymentMethod.choices)

    is_recurring = models.BooleanField(default=False, verbose_name="Recorrente?")
    recurrence_start = models.DateField(
        null=True, blank=True, verbose_name="Início da recorrência")
    recurrence_end = models.DateField(
        null=True, blank=True, verbose_name="Fim da recorrência")
    recurrence_frequency = models.CharField(
        max_length=10,
        choices=Frequency.choices,
        blank=True,
        default="",
        verbose_name="Frequência da recorrência",
    )


    class Meta:
        ordering = ["-date"]
        verbose_name = "Transaction"
        verbose_name_plural = "Transactions"
        abstract = True

    def __str__(self) -> str:
        return f"{self.value} - {self.date} - {self.description}"

    def generate_transactions(self):
        """
        Gera as transações reais a partir da recorrente.
        Pode ser chamado mensalmente via Celery para criar as novas transações.
        """
        pass  # Aqui entra a lógica de gerar a transação real


class Income(Transaction):

    payment_proof = models.ImageField(
        upload_to="payment_proofs/income/", blank=True, null=True)
    balance = models.ForeignKey(
        Balance, on_delete=models.CASCADE, null=True, blank=True,
        related_name="incomes",
        verbose_name="Balanço",
    )
    class Meta:
        verbose_name = "Income"
        verbose_name_plural = "Incomes"


class Expense(Transaction):
    payment_proof = models.ImageField(
        upload_to="payment_proofs/expense/", blank=True, null=True)
    balance = models.ForeignKey(
        Balance, on_delete=models.CASCADE, null=True, blank=True,
        related_name="expenses",
        verbose_name="Balanço",
    )

    class Meta:
        verbose_name = "Expense"
        verbose_name_plural = "Expenses"

