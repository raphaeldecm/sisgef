from django.contrib.auth.models import Group,Permission
from django.core.management.base import BaseCommand
from django.utils.translation import gettext_lazy as _


class Command(BaseCommand):
    help = """
        Cria grupos de perfil de usuário: Gestor e Secretário,
        e define as permissões associadas.
    """

    def handle(self, *args, **options):
   
        perfil_grupos = {
            "Gestor": Permission.objects.all(),  
            "Secretário": Permission.objects.filter(
                codename__in=[
                    # Receitas
                    "add_income", "change_income", "view_income",
                    # Despesas
                    "add_expense", "change_expense", "view_expense",
                    # Categorias
                    "add_category", "change_category", "delete_category", "view_category",
                ]
            ),
        }

        for group_name, permissoes in perfil_grupos.items():
            group, created = Group.objects.get_or_create(name=_(group_name))
            group.permissions.set(permissoes)
            self.stdout.write(f"Grupo '{group_name}' atualizado com {'criação' if created else 'sucesso'}.")

        self.stdout.write(self.style.SUCCESS("Grupos de perfil e permissões configurados com sucesso."))