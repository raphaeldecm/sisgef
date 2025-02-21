from django.shortcuts import render
from django.views.generic import TemplateView

from sisgef.core.mixins import TitleViewMixin


class IncomeListView(TitleViewMixin, TemplateView):
    template_name = "income/income_list.html"
    title = "Receitas"
    subtitle = "Lista de receitas."


class ExpenseListView(TitleViewMixin, TemplateView):
    template_name = "expense/expense_list.html"
    title = "Despesas"
    subtitle = "Lista de Despesas."

class CategoryListView(TitleViewMixin, TemplateView):
    template_name = "category/category_list.html"
    title = "Categorias de Receitas e Despesas"
    subtitle = "Lista de Categorias de Receitas e Despesas"
