from django.contrib import admin

from .models import Articulo, Autor, Comentario, Pagina


@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ("nombre", "apellido", "email")


@admin.register(Articulo)
class ArticuloAdmin(admin.ModelAdmin):
    list_display = ("titulo", "autor", "fecha_publicacion")
    list_filter = ("autor", "fecha_publicacion")
    search_fields = ("titulo", "cuerpo")


@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ("nombre_usuario", "articulo", "fecha")
    list_filter = ("fecha",)


@admin.register(Pagina)
class PaginaAdmin(admin.ModelAdmin):
    list_display = ("titulo", "autor", "fecha")
    list_filter = ("autor", "fecha")
    search_fields = ("titulo", "subtitulo", "cuerpo")

