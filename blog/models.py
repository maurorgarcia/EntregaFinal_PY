from django.contrib.auth.models import User
from django.db import models
from ckeditor.fields import RichTextField


class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()
    bio = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.nombre} {self.apellido}"

    class Meta:
        verbose_name_plural = "Autores"


class Articulo(models.Model):
    titulo = models.CharField(max_length=200)
    subtitulo = models.CharField(max_length=300, null=True, blank=True)
    cuerpo = models.TextField()
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, related_name="articulos")

    def __str__(self) -> str:
        return self.titulo

    class Meta:
        verbose_name_plural = "Artículos"
        ordering = ["-fecha_publicacion"]


class Comentario(models.Model):
    articulo = models.ForeignKey(
        Articulo, on_delete=models.CASCADE, related_name="comentarios"
    )
    nombre_usuario = models.CharField(max_length=100)
    contenido = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.nombre_usuario} - {self.articulo}"

    class Meta:
        ordering = ["-fecha"]


class Pagina(models.Model):
    # Modelo principal del proyecto final (Pages):
    # - 2 x CharField: titulo, subtitulo
    # - RichText: cuerpo (ckeditor)
    # - ImageField: imagen
    # - DateTime: fecha
    titulo = models.CharField(max_length=200)
    subtitulo = models.CharField(max_length=200)
    cuerpo = RichTextField()
    autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="paginas")
    fecha = models.DateTimeField(auto_now_add=True)
    imagen = models.ImageField(upload_to="pages/", null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.titulo} - {self.autor}"

    class Meta:
        verbose_name = "Página"
        verbose_name_plural = "Páginas"
        ordering = ["-fecha"]
