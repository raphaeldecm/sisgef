from decimal import Decimal

from django import forms

from . import models


class CategoryForm(forms.ModelForm):
    class Meta:
        model = models.Category
        fields = ["name", "description", "type"]
        labels = {
            "name": "Nome",
            "description": "Descrição",
            "type": "Tipo",
        }

class ExpenseForm(forms.ModelForm):

    category = forms.ModelChoiceField(
        label="Categoria",
        queryset=models.Category.objects.filter(type=models.Category.Type.EXPENSE),
    )
    value = forms.CharField(
        label="Valor",
        required=True,
    )

    def clean_value(self):
        value = self.cleaned_data["value"]
        return Decimal(value.replace(",", "."))

    def clean_payment_proof(self):
        payment_proof = self.cleaned_data.get("payment_proof")
        if not payment_proof:
            return self.instance.payment_proof
        return payment_proof

    class Meta:
        model = models.Expense
        fields = ["date", "category", "description", "value", "payment_proof",
                  "payment_method", "status"]
        labels = {
            "date": "Data",
            "category": "Categoria",
            "description": "Descrição",
            "value": "Valor",
            "payment_proof": "Comprovante de Pagamento",
            "payment_method": "Método de Pagamento",
            "status": "Situação",
        }

class IncomeForm(forms.ModelForm):

    category = forms.ModelChoiceField(
        label="Categoria",
        queryset=models.Category.objects.filter(type=models.Category.Type.INCOME),
    )
    value = forms.CharField(
        label="Valor",
        required=True,
    )

    def clean_value(self):
        value = self.cleaned_data["value"]
        return Decimal(value.replace(",", "."))

    def clean_payment_proof(self):
        payment_proof = self.cleaned_data.get("payment_proof")
        if not payment_proof:
            return self.instance.payment_proof
        return payment_proof

    class Meta:
        model = models.Income
        fields = ["date", "category", "description", "value", "payment_proof",
                  "payment_method", "status"]
        labels = {
            "date": "Data",
            "category": "Categoria",
            "description": "Descrição",
            "value": "Valor",
            "payment_proof": "Comprovante de Pagamento",
            "payment_method": "Método de Pagamento",
            "status": "Situação",
        }
