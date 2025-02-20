from django.contrib import messages
from django.db.models.deletion import ProtectedError
from django.shortcuts import redirect


class TitleViewMixin:
    title = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = self.title
        return context


class ProtectedErrorMessageMixin:
    protected_warning_message = ""

    def form_valid(self, form):
        try:
            return super().form_valid(form)
        except ProtectedError:
            messages.warning(self.request, self.protected_warning_message)
            return redirect(self.request.headers.get("referer"))
