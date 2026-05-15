from django.shortcuts import render, redirect
from django.db.models import Q
from .models import Autor, Articulo, Comentario
from .forms import AutorForm, ArticuloForm, ComentarioForm, BusquedaArticuloForm

# Inicio del blog
def inicio(request):
    articulos = Articulo.objects.all()[:5]
    return render(request, 'blog/inicio.html', {'articulos': articulos})

# Vistas para crear autores, articulos y comentarios
def crear_autor(request):
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'blog/exito.html', {
                'mensaje': 'Autor creado exitosamente',
                'tipo': 'autor',
            })
    else:
        form = AutorForm()
    return render(request, 'blog/crear_autor.html', {'form': form})

def crear_articulo(request):
    if request.method == 'POST':
        form = ArticuloForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'blog/exito.html', {
                'mensaje': 'Artículo publicado exitosamente',
                'tipo': 'articulo',
            })
    else:
        form = ArticuloForm()
    return render(request, 'blog/crear_articulo.html', {'form': form})

def crear_comentario(request):
    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'blog/exito.html', {
                'mensaje': 'Comentario agregado exitosamente',
                'tipo': 'comentario',
            })
    else:
        form = ComentarioForm()
    return render(request, 'blog/crear_comentario.html', {'form': form})

# Buscador de articulos
def buscar_articulos(request):
    form = BusquedaArticuloForm(request.GET or None)
    resultados = None

    if form.is_valid():
        query = form.cleaned_data['query']
        resultados = Articulo.objects.filter(
            Q(titulo__icontains=query) | Q(cuerpo__icontains=query)
        )

    return render(request, 'blog/buscar.html', {
        'form': form,
        'resultados': resultados,
    })
