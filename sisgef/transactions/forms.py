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
        queryset=models.Category.objects.filter(type=models.Category.Type.EXPENSE),
    )

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
