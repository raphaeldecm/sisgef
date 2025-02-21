from django_filters import rest_framework as django_filters

from sisgef.transactions.models import Category


class CategoryFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr="icontains", label="Nome")
    description = django_filters.CharFilter(lookup_expr="icontains", label="Descrição")
    category_type = django_filters.ChoiceFilter(
        choices=Category.Type.choices,
        label="Categoria",
    )

    class Meta:
        model = Category
        fields = ["name", "description", "category_type"]
