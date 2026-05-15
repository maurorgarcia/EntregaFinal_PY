from django.db import models
from django.contrib.auth.models import User

class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatares/', null=True, blank=True)
    biografia = models.TextField(max_length=500, blank=True)
    link = models.URLField(max_length=200, blank=True)

    def __str__(self):
        return f"Perfil de {self.user.username}"
