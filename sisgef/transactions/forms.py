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
