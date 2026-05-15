from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('crear-autor/', views.crear_autor, name='crear_autor'),
    path('crear-articulo/', views.crear_articulo, name='crear_articulo'),
    path('crear-comentario/', views.crear_comentario, name='crear_comentario'),
    path('buscar/', views.buscar_articulos, name='buscar'),
]
