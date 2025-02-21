from django.views import generic
from django_filters.views import FilterView

from sisgef.core import constants
from sisgef.core.mixins import TitleViewMixin

from . import models


class IncomeListView(TitleViewMixin, generic.TemplateView):
    template_name = "income/income_list.html"
    title = "Receitas"
    subtitle = "Lista de receitas."


class ExpenseListView(TitleViewMixin, generic.TemplateView):
    template_name = "expense/expense_list.html"
    title = "Despesas"
    subtitle = "Lista de Despesas."

class CategoryListView(TitleViewMixin, FilterView, generic.ListView):
    model = models.Category
    paginate_by = constants.DEFAULT_PAGE_SIZE
    template_name = "category/category_list.html"
    title = "Categorias"
    subtitle = "Gerenciamento de Categorias de Receitas e Despesas"
