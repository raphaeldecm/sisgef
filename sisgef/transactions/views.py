from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views import generic
from django_filters.views import FilterView

from sisgef.core import constants
from sisgef.core.mixins import ProtectedErrorMessageMixin
from sisgef.core.mixins import TitleViewMixin

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
