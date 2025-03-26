from django.urls import path

from . import views

app_name = "transactions"

urlpatterns = [
  path("income/list/", view=views.IncomeListView.as_view(), name="income_list"),
    path(
        "income/create/",
        view=views.IncomeCreateView.as_view(),
        name="income_create",
    ),
    path(
        "income/update/<int:pk>/",
        view=views.IncomeUpdateView.as_view(),
        name="income_update",
    ),
    path(
        "income/delete/<int:pk>/",
        view=views.IncomeDeleteView.as_view(),
        name="income_delete",
    ),
    path(
        "income/detail/<int:pk>/",
        view=views.IncomeDetailView.as_view(),
        name="income_detail",
    ),
  path("expense/list/", view=views.ExpenseListView.as_view(), name="expense_list"),
    path(
        "expense/create/",
        view=views.ExpenseCreateView.as_view(),
        name="expense_create",
    ),
    path(
        "expense/update/<int:pk>/",
        view=views.ExpenseUpdateView.as_view(),
        name="expense_update",
    ),
    path(
        "expense/delete/<int:pk>/",
        view=views.ExpenseDeleteView.as_view(),
        name="expense_delete",
    ),
    path(
        "expense/detail/<int:pk>/",
        view=views.ExpenseDetailView.as_view(),
        name="expense_detail",
    ),
  path("category/list/", view=views.CategoryListView.as_view(), name="category_list"),
  path(
    "category/delete/<int:pk>/",
    view=views.CategoryDeleteView.as_view(),
    name="category_delete",
),
    path(
    "category/create/",
    view=views.CategoryCreateView.as_view(),
    name="category_create",
),
    path(
    "category/update/<int:pk>/",
    view=views.CategoryUpdateView.as_view(),
    name="category_update",
),
path(
  "category/detail/<int:pk>/",
  view=views.CategoryDetailView.as_view(),
  name="category_detail",
),
]
