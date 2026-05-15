from django.urls import path

from . import views

app_name = "blog"

urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("about/", views.AboutView.as_view(), name="about"),
    path("pages/", views.PaginaListView.as_view(), name="pages"),
    path("pages/create/", views.PaginaCreateView.as_view(), name="page_create"),
    path("pages/<int:pk>/", views.PaginaDetailView.as_view(), name="page_detail"),
    path("pages/<int:pk>/edit/", views.PaginaUpdateView.as_view(), name="page_update"),
    path("pages/<int:pk>/delete/", views.PaginaDeleteView.as_view(), name="page_delete"),
    path("crear-autor/", views.crear_autor, name="crear_autor"),
    path("crear-articulo/", views.crear_articulo, name="crear_articulo"),
    path("crear-comentario/", views.crear_comentario, name="crear_comentario"),
    path("buscar/", views.buscar_articulos, name="buscar"),
]
