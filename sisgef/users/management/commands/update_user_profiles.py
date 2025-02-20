from django.contrib.auth.models import Group
from django.core.management.base import BaseCommand
from django.utils.translation import gettext_lazy as _


class Command(BaseCommand):
    help = """
        Create django groups to represent user profiles,
        based in models using decorator 'profile'
    """

    def handle(self, *args, **options):
        profile_groups = set()
        profile_groups.add("Gerente")
        profile_groups.add("Colaborador")
        for group_name in profile_groups:
            group, created = Group.objects.get_or_create(name=_(group_name))
        self.stdout.write("Profile groups were updated successfully")
