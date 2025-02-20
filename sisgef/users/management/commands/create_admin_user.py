from django.contrib.auth import get_user_model
from django.contrib.auth import models
from django.core.management.base import BaseCommand

User = get_user_model()


class Command(BaseCommand):
    ADMIN_NAME = "admin"
    ADMIN_EMAIL = "admin@sisgef.com.br"
    ADMIN_PASSWORD = (
        "argon2$argon2id$v=19$m=102400,t=2,p=8$dFJCaGljNzhyUTNuZk94UG5hSExNYw"  # noqa: S105
        "$TPa9rRWrUtHNJUoy5VylND9EgWFfvzh/G4HpOHoZmXM"
    )
    help = "Adding superuser..."

    def handle(self, *args, **options):
        if User.objects.filter(is_superuser=True).exists():
            self.stdout.write("The superuser already exists")
        else:
            group = models.Group.objects.get(name="Gerente")
            user = User.objects.create(
                name=self.ADMIN_NAME,
                email=self.ADMIN_EMAIL,
                password=self.ADMIN_PASSWORD,
                is_superuser=True,
                is_staff=True,
            )
            user.groups.add(group)
