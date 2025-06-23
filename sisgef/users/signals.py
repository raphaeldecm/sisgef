from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models.signals import post_migrate
from allauth.account.signals import user_signed_up

User = get_user_model()

@receiver(post_save, sender=User)
def add_user_to_default_group(sender, instance, created, **kwargs):
    if created:
        group, _ = Group.objects.get_or_create(name="Colaborador")
        instance.groups.add(group)


@receiver(post_migrate)
def create_standard_groups(sender, **kwargs):
    if sender.name != 'users':  
        return

    Group.objects.get_or_create(name='Secretário')
    Group.objects.get_or_create(name='Gestor')

@receiver(user_signed_up)
def congigure_new_user_group(request, user, **kwargs):
    try:
        grupo = Group.objects.get(name='Secretário')
        user.groups.add(grupo)
        user.is_active = False
        user.save()
    except Exception as e: # Catches any other unexpected exceptions
        print(f"An unexpected error occurred on group: {e}")

    
    