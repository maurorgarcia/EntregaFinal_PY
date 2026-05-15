from django.contrib import admin

from .models import Mensaje


@admin.register(Mensaje)
class MensajeAdmin(admin.ModelAdmin):
    list_display = ("emisor", "receptor", "fecha")
    search_fields = ("contenido", "emisor__username", "receptor__username")
