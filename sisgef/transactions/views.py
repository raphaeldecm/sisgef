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
