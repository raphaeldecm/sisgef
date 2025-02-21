from django.shortcuts import render
from django.views.generic import TemplateView

from .mixins import TitleViewMixin


class DashboardView(TitleViewMixin, TemplateView):
    template_name = "core/dashboard.html"
    title = "Dashboard"
    subtitle = "Bem-vindo ao Sistema de Gestão Financeira"
