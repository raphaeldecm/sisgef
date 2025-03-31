from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import resolve_url
from django.shortcuts import reverse
from django.urls import reverse_lazy
from django.views import generic
from django_filters.views import FilterView

from sisgef.core import constants
from sisgef.core.mixins import ProtectedErrorMessageMixin
from sisgef.core.mixins import TitleViewMixin
from sisgef.transactions import forms

from . import filters
from . import models


class TransactionListView(generic.ListView):
    template_name = "transaction/transaction_list.html"
    paginate_by = constants.DEFAULT_PAGE_SIZE
    ordering = ["-date"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        transaction_type = self.model.__name__.lower()  # 'income' ou 'expense'
        context["transaction_type"] = transaction_type
        context["create_url"] = resolve_url(f"transactions:{transaction_type}_create")
        context["delete_url"] = f"transactions:{transaction_type}_delete"
        context["detail_url"] = f"transactions:{transaction_type}_detail"
        context["update_url"] = f"transactions:{transaction_type}_update"

        return context

class IncomeListView(TitleViewMixin, FilterView, TransactionListView):
    model = models.Income
    filterset_class = filters.IncomeFilter
    title = "Receitas"
    subtitle = "Gerenciamento de receitas."

class ExpenseListView(TitleViewMixin, FilterView, TransactionListView):
    model = models.Expense
    filterset_class = filters.ExpenseFilter
    title = "Despesas"
    subtitle = "Gerenciamento de Despesas."

class TransactionTemplateFormView(
    TitleViewMixin,
    SuccessMessageMixin,
):
    template_name = "transaction/transaction_form.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["transaction_type"] = self.model.__name__.lower()
        context["return_url"] = resolve_url(
            f"transactions:{context['transaction_type']}_list",
            )
        return context

class IncomeCreateView(TransactionTemplateFormView, generic.CreateView):
    model = models.Income
    form_class = forms.IncomeForm
    title = "Nova Receita"
    subtitle = "Cadastro de nova receita."
    success_url = reverse_lazy("transactions:income_list")
    success_message = "Receita cadastrada com sucesso."

class ExpenseCreateView(TransactionTemplateFormView, generic.CreateView):
    model = models.Expense
    form_class = forms.ExpenseForm
    title = "Nova Despesa"
    subtitle = "Cadastro de nova despesa."
    success_url = reverse_lazy("transactions:expense_list")
    success_message = "Despesa cadastrada com sucesso."

class IncomeUpdateView(
    TransactionTemplateFormView,
    generic.UpdateView,
):
    model = models.Income
    form_class = forms.IncomeForm
    title = "Atualizar Receita"
    subtitle = "Atualização de receita."
    success_url = reverse_lazy("transactions:income_list")
    success_message = "Receita atualizada com sucesso."

class ExpenseUpdateView(
    TransactionTemplateFormView,
    generic.UpdateView,
):
    model = models.Expense
    form_class = forms.ExpenseForm
    title = "Atualizar Despesa"
    subtitle = "Atualização de despesa."
    success_url = reverse_lazy("transactions:expense_list")
    success_message = "Despesa atualizada com sucesso."

class IncomeDeleteView(
    SuccessMessageMixin,
    generic.DeleteView,
):
    model = models.Income
    success_url = reverse_lazy("transactions:income_list")
    success_message = "Receita excluída com sucesso."

class TrancsactionDetailView(
    TitleViewMixin,
    generic.DetailView,
):
    template_name = "transaction/transaction_detail.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["transaction_type"] = self.model.__name__.lower()
        return context

class IncomeDetailView(TrancsactionDetailView):
    model = models.Income
    title = "Detalhes da Receita"
    subtitle = "Informações de cadastro da receita."

class ExpenseDetailView(TrancsactionDetailView):
    model = models.Expense
    title = "Detalhes da Despesa"
    subtitle = "Informações de cadastro da despesa."


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
