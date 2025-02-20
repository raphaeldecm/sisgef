from django.urls import path

from .views import user_detail_view
from .views import user_redirect_view
from .views import user_update_view
from .views import DashboardView, RelatoriosView
app_name = "users"
urlpatterns = [
    path("~redirect/", view=user_redirect_view, name="redirect"),
    path("~update/", view=user_update_view, name="update"),
    path("<int:pk>/", view=user_detail_view, name="detail"),
    path("dashboard/", view=DashboardView.as_view(), name="dashboard"),
    path("relatorios/", view=RelatoriosView.as_view(), name="relatorios"),
]
