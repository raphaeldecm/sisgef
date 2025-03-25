from decimal import Decimal
from decimal import InvalidOperation

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
    date_from = django_filters.DateFilter(
        field_name="date", lookup_expr="gte", label="De")
    date_to = django_filters.DateFilter(
        field_name="date", lookup_expr="lte", label="Até")
    category = django_filters.ModelChoiceFilter(
        queryset=Category.objects.filter(type=Category.Type.EXPENSE),
        label="Categoria",
    )
    value_from = django_filters.CharFilter(
        field_name="value", method="filter_value_from", label="De")
    value_to = django_filters.CharFilter(
        field_name="value", method="filter_value_to", label="Até")
    status = django_filters.ChoiceFilter(
        choices=Expense.PaymentStatus.choices,
        label="Situação",
    )

    def filter_value_from(self, queryset, name, value):
        try:
            clean_value = Decimal(value.replace(",", "."))  # Converte "1.234,56" para Decimal
            return queryset.filter(**{f"{name}__gte": clean_value})
        except (ValueError, InvalidOperation):
            return queryset  # Se a conversão falhar, retorna o queryset original

    def filter_value_to(self, queryset, name, value):
        try:
            clean_value = Decimal(value.replace(",", "."))
            return queryset.filter(**{f"{name}__lte": clean_value})
        except (ValueError, InvalidOperation):
            return queryset

    class Meta:
        model = Expense
        fields = ["description", "date", "category", "status"]
