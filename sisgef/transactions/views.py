from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic import TemplateView

from sisgef.core import constants
from sisgef.core.mixins import TitleViewMixin

from . import models


class IncomeListView(TitleViewMixin, TemplateView):
    template_name = "income/income_list.html"
    title = "Receitas"
    subtitle = "Lista de receitas."


class ExpenseListView(TitleViewMixin, TemplateView):
    template_name = "expense/expense_list.html"
    title = "Despesas"
    subtitle = "Lista de Despesas."

class CategoryListView(TitleViewMixin, ListView):
    model = models.Category
    paginate_by = constants.DEFAULT_PAGE_SIZE
    template_name = "category/category_list.html"
    title = "Categorias de Receitas e Despesas"
    subtitle = "Gerenciamento de Categorias de Receitas e Despesas"
