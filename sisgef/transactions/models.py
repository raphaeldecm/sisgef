from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

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

    description = models.TextField(verbose_name="Descrição")
    value = models.DecimalField(verbose_name="Valor", max_digits=6, decimal_places=2)
    date = models.DateTimeField()
    payment_proof = models.ImageField(upload_to="payment_proofs/", blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    payment_method = models.CharField(max_length=2, choices=PaymentMethod.choices)

    class Meta:
        ordering = ["-date"]
        verbose_name = "Transaction"
        verbose_name_plural = "Transactions"
        abstract = True

    def __str__(self) -> str:
        return f"{self.value} - {self.date} - {self.description}"

class Income(Transaction):
    class Meta:
        verbose_name = "Income"
        verbose_name_plural = "Incomes"

class Expense(Transaction):
    class PaymentStatus(models.TextChoices):
        PENDING = "PD", _("Pendente")
        PAID = "PA", _("Pago")
        CANCELED = "CA", _("Cancelado")
        OVERDUE = "OV", _("Atrasado")

    status = models.CharField(max_length=10, choices=PaymentStatus.choices)

    class Meta:
        verbose_name = "Expense"
        verbose_name_plural = "Expenses"
