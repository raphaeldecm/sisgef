from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

from sisgef.core.constants import MAX_CHAR_FIELD_NAME_LENGTH
from sisgef.core.models import BaseModel

User = get_user_model()

class Type(models.TextChoices):
        INCOME = "IN", _("Income")
        EXPENSE = "EX", _("Expense")

class Category(BaseModel):
    name = models.CharField(max_length=MAX_CHAR_FIELD_NAME_LENGTH)
    description = models.TextField()
    category_type = models.CharField(max_length=2, choices=Type.choices)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self) -> str:
        return self.name


class Transaction(BaseModel):
    description = models.TextField()
    value = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField()
    payment_proof = models.ImageField(upload_to="payment_proofs/")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

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
    class Meta:
        verbose_name = "Expense"
        verbose_name_plural = "Expenses"
