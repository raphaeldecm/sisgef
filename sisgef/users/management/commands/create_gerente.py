from django.contrib.auth.models import Group, Permission, User

gerente, created = Group.objects.get_or_create(name="Gerente")


perm = Permission.objects.get(codename="change_user", content_type__app_label="auth")
gerente.permissions.add(perm)

user = User.objects.get(username="nome_do_usuario")  # ou filter(email="…")
user.groups.add(gerente)
user.save()