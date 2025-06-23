from django.shortcuts import redirect
from django.core.exceptions import PermissionDenied

class RestrictAdminToGerentes:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.startswith('/admin/') and request.user.is_authenticated:
            if not request.user.groups.filter(name="Gerente").exists():
                raise PermissionDenied("Apenas gerentes podem acessar o admin.")
        return self.get_response(request)