from django import forms
from .models import Autor, Articulo, Comentario

# Formularios del blog
class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['nombre', 'apellido', 'email', 'bio']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'bio': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }

class ArticuloForm(forms.ModelForm):
    class Meta:
        model = Articulo
        fields = ['titulo', 'subtitulo', 'cuerpo', 'autor']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'subtitulo': forms.TextInput(attrs={'class': 'form-control'}),
            'cuerpo': forms.Textarea(attrs={'class': 'form-control', 'rows': 6}),
            'autor': forms.Select(attrs={'class': 'form-control'}),
        }

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['articulo', 'nombre_usuario', 'contenido']
        widgets = {
            'articulo': forms.Select(attrs={'class': 'form-control'}),
            'nombre_usuario': forms.TextInput(attrs={'class': 'form-control'}),
            'contenido': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }

class BusquedaArticuloForm(forms.Form):
    query = forms.CharField(
        max_length=200,
        label='Buscar',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Escribí acá para buscar...',
        })
    )
