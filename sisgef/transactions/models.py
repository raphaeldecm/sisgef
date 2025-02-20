from django.contrib.auth import get_user_model
from django.db import models

from sisgef.core.constants import MAX_CHAR_FIELD_NAME_LENGTH
from sisgef.core.models import BaseModel

User = get_user_model()

class Category(models.Model):
    name = models.CharField(max_length=MAX_CHAR_FIELD_NAME_LENGTH)
    description = models.TextField()

    def __str__(self) -> str:
        return self.name


class Transaction(BaseModel):
    class Type(models.TextChoices):
        INCOME = "IN", "Income"
        EXPENSE = "EX", "Expense"

    transaction_type = models.CharField(max_length=2, choices=Type.choices)
    description = models.TextField()
    value = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField()
    payment_proof = models.ImageField(upload_to="payment_proofs/")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        ordering = ["-date"]

    def __str__(self) -> str:
        return f"{self.value} - {self.date} - {self.description}"
