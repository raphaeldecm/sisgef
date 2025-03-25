from django_filters import rest_framework as django_filters

from sisgef.transactions.models import Category
from sisgef.transactions.models import Expense


class CategoryFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr="icontains", label="Nome")
    description = django_filters.CharFilter(lookup_expr="icontains", label="Descrição")
    type = django_filters.ChoiceFilter(
        choices=Category.Type.choices,
        label="Categoria",
    )

    class Meta:
        model = Category
        fields = ["name", "description", "type"]

class ExpenseFilter(django_filters.FilterSet):
    description = django_filters.CharFilter(lookup_expr="icontains", label="Descrição")
    date = django_filters.DateFromToRangeFilter(label="Data")
    category = django_filters.ModelChoiceFilter(
        queryset=Category.objects.filter(type=Category.Type.EXPENSE),
        label="Categoria",
    )
    value = django_filters.NumericRangeFilter(label="Valor")
    status = django_filters.ChoiceFilter(
        choices=Expense.PaymentStatus.choices,
        label="Situação",
    )

    class Meta:
        model = Expense
        fields = ["description", "date", "category", "value", "status"]
