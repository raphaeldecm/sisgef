from django.urls import path

from . import views

app_name = "transactions"

urlpatterns = [
  path("income/list/", view=views.IncomeListView.as_view(), name="income_list"),
  path("expense/list/", view=views.ExpenseListView.as_view(), name="expense_list"),
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
]
