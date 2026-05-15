from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Q
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView

from .forms import (
    ArticuloForm,
    AutorForm,
    BusquedaArticuloForm,
    ComentarioForm,
    PaginaForm,
)
from .models import Articulo, Autor, Comentario, Pagina


def inicio(request):
    # Home del blog: muestra los últimos artículos creados.
    articulos = Articulo.objects.all()[:5]
    return render(request, "blog/inicio.html", {"articulos": articulos})


def crear_autor(request):
    if request.method == "POST":
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return render(
                request,
                "blog/exito.html",
                {
                    "mensaje": "Autor creado exitosamente",
                    "tipo": "autor",
                },
            )
    else:
        form = AutorForm()
    return render(request, "blog/crear_autor.html", {"form": form})


def crear_articulo(request):
    if request.method == "POST":
        form = ArticuloForm(request.POST)
        if form.is_valid():
            form.save()
            return render(
                request,
                "blog/exito.html",
                {
                    "mensaje": "Artículo publicado exitosamente",
                    "tipo": "articulo",
                },
            )
    else:
        form = ArticuloForm()
    return render(request, "blog/crear_articulo.html", {"form": form})


def crear_comentario(request):
    if request.method == "POST":
        form = ComentarioForm(request.POST)
        if form.is_valid():
            form.save()
            return render(
                request,
                "blog/exito.html",
                {
                    "mensaje": "Comentario agregado exitosamente",
                    "tipo": "comentario",
                },
            )
    else:
        form = ComentarioForm()
    return render(request, "blog/crear_comentario.html", {"form": form})


def buscar_articulos(request):
    # Buscador simple para Articulo; sirve como ejemplo de view "común"
    # (no CBV) que procesa un form por GET.
    form = BusquedaArticuloForm(request.GET or None)
    resultados = None

    if form.is_valid():
        query = form.cleaned_data["query"]
        resultados = Articulo.objects.filter(
            Q(titulo__icontains=query) | Q(cuerpo__icontains=query)
        )

    return render(
        request,
        "blog/buscar.html",
        {
            "form": form,
            "resultados": resultados,
        },
    )


class AboutView(TemplateView):
    # Vista estática "Acerca de mí" requerida por la consigna en /about/
    template_name = "blog/about.html"


class PaginaListView(ListView):
    # Listado de Pages en /pages/ con búsqueda opcional por querystring (?q=...).
    model = Pagina
    template_name = "blog/pages_list.html"
    context_object_name = "paginas"
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        q = (self.request.GET.get("q") or "").strip()
        if not q:
            return queryset
        return queryset.filter(
            Q(titulo__icontains=q) | Q(subtitulo__icontains=q) | Q(cuerpo__icontains=q)
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["q"] = (self.request.GET.get("q") or "").strip()
        return context


class PaginaDetailView(DetailView):
    # Detalle de una Page en /pages/<id>/ (desde "Leer más" en el listado).
    model = Pagina
    template_name = "blog/page_detail.html"
    context_object_name = "pagina"


class PaginaCreateView(LoginRequiredMixin, CreateView):
    # Crear una Page (solo logueado). El autor se setea automáticamente con request.user.
    model = Pagina
    form_class = PaginaForm
    template_name = "blog/page_form.html"
    success_url = reverse_lazy("blog:pages")

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)


class PaginaUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    # Editar una Page (solo logueado y solo si sos el autor).
    # UserPassesTestMixin es el "mixin" pedido: restringe permisos por objeto.
    model = Pagina
    form_class = PaginaForm
    template_name = "blog/page_form.html"

    def test_func(self):
        pagina = self.get_object()
        return pagina.autor_id == self.request.user.id

    def get_success_url(self):
        return reverse_lazy("blog:page_detail", kwargs={"pk": self.object.pk})


class PaginaDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    # Borrar una Page (solo logueado y solo si sos el autor).
    model = Pagina
    template_name = "blog/page_confirm_delete.html"
    success_url = reverse_lazy("blog:pages")

    def test_func(self):
        pagina = self.get_object()
        return pagina.autor_id == self.request.user.id
