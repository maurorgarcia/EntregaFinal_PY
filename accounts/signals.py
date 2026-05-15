from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Perfil


@receiver(post_save, sender=User)
def crear_perfil(sender, instance, created, **kwargs):
    # Crea automáticamente el Perfil cuando se registra un User.
    # Esto simplifica la lógica del signup y evita perfiles "faltantes".
    if created:
        Perfil.objects.create(user=instance)
