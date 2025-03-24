from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views import generic
from django_filters.views import FilterView

from sisgef.core import constants
from sisgef.core.mixins import ProtectedErrorMessageMixin
from sisgef.core.mixins import TitleViewMixin
from sisgef.transactions import forms

from . import filters
from . import models


class IncomeListView(TitleViewMixin, generic.TemplateView):
    template_name = "income/income_list.html"
    title = "Receitas"
    subtitle = "Lista de receitas."


class ExpenseListView(TitleViewMixin, generic.ListView):
    model = models.Expense
    paginate_by = constants.DEFAULT_PAGE_SIZE
    template_name = "expense/expense_list.html"
    title = "Despesas"
    subtitle = "Gerenciamento de Despesas."
    ordering = ["-date"]

class ExpenseCreateView(
    TitleViewMixin,
    SuccessMessageMixin,
    generic.CreateView,
):
    model = models.Expense
    form_class = forms.ExpenseForm
    template_name = "expense/expense_form.html"
    title = "Nova Despesa"
    subtitle = "Cadastro de nova despesa."
    success_url = reverse_lazy("transactions:expense_list")
    success_message = "Despesa cadastrada com sucesso."

class ExpenseUpdateView(
    TitleViewMixin,
    SuccessMessageMixin,
    generic.UpdateView,
):
    model = models.Expense
    form_class = forms.ExpenseForm
    template_name = "expense/expense_form.html"
    title = "Atualizar Despesa"
    subtitle = "Atualização de despesa."
    success_url = reverse_lazy("transactions:expense_list")
    success_message = "Despesa atualizada com sucesso."

class ExpenseDeleteView(
    SuccessMessageMixin,
    generic.DeleteView,
):
    model = models.Expense
    success_url = reverse_lazy("transactions:expense_list")
    success_message = "Despesa excluída com sucesso."


class CategoryListView(TitleViewMixin, FilterView, generic.ListView):
    model = models.Category
    paginate_by = constants.DEFAULT_PAGE_SIZE
    template_name = "category/category_list.html"
    title = "Categorias"
    subtitle = "Gerenciamento de Categorias de Receitas e Despesas"
    filterset_class = filters.CategoryFilter
    ordering = ["name"]

class CategoryDeleteView(
    ProtectedErrorMessageMixin,
    SuccessMessageMixin,
    generic.DeleteView,
):
    model = models.Category
    success_url = reverse_lazy("transactions:category_list")
    success_message = "Categoria excluída com sucesso."
    protected_warning_message = (
        "Não é possível excluir uma categoria que está sendo "
        "utilizada em uma transação."
    )

class CategoryCreateView(
    TitleViewMixin,
    SuccessMessageMixin,
    generic.CreateView,
):
    model = models.Category
    form_class= forms.CategoryForm
    template_name = "category/category_form.html"
    title = "Nova Categoria"
    subtitle = "Cadastro de nova categoria."
    success_url = reverse_lazy("transactions:category_list")
    success_message = "Categoria cadastrada com sucesso."

class CategoryUpdateView(
    TitleViewMixin,
    SuccessMessageMixin,
    generic.UpdateView,
):
    model = models.Category
    form_class = forms.CategoryForm
    template_name = "category/category_form.html"
    title = "Atualizar Categoria"
    subtitle = "Atualização de categoria."
    success_url = reverse_lazy("transactions:category_list")
    success_message = "Categoria atualizada com sucesso."

class CategoryDetailView(TitleViewMixin, generic.DetailView):
    model = models.Category
    template_name = "category/category_detail.html"
    title = "Detalhes da Categoria"
    subtitle = "Informações de cadastro da categoria."
