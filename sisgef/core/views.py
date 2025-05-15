from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

from .mixins import TitleViewMixin


class DashboardView(LoginRequiredMixin, TitleViewMixin, TemplateView):
    template_name = "core/dashboard.html"
    title = "Dashboard"
    subtitle = "Bem-vindo ao Sistema de Gestão Financeira"
