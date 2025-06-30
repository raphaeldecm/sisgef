from django.contrib.auth.mixins import AccessMixin
from django.shortcuts import redirect

class GroupRequiredMixin(AccessMixin):
    group_required = None 

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()

        required = self.group_required
        if isinstance(required, str):
            required = [required]

        if not request.user.groups.filter(name__in=required).exists():
            return redirect("home")  # ou qualquer outra URL nomeada

        return super().dispatch(request, *args, **kwargs)