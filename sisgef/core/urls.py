from django.urls import path

from .views import DashboardView

app_name = "users"

urlpatterns = [
    path("", view=DashboardView.as_view(), name="dashboard"),
]
