from django.contrib import admin
from .models import Autor, Articulo, Comentario


@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'email')


@admin.register(Articulo)
class ArticuloAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'fecha_publicacion')
    list_filter = ('autor', 'fecha_publicacion')
    search_fields = ('titulo', 'cuerpo')


@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('nombre_usuario', 'articulo', 'fecha')
    list_filter = ('fecha',)
