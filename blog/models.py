from django.db import models


class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()
    bio = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "Autores"

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Articulo(models.Model):
    titulo = models.CharField(max_length=200)
    subtitulo = models.CharField(max_length=300, blank=True, null=True)
    cuerpo = models.TextField()
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, related_name='articulos')
    fecha_publicacion = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-fecha_publicacion']
        verbose_name_plural = "Artículos"

    def __str__(self):
        return self.titulo


class Comentario(models.Model):
    articulo = models.ForeignKey(Articulo, on_delete=models.CASCADE, related_name='comentarios')
    nombre_usuario = models.CharField(max_length=100)
    contenido = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-fecha']

    def __str__(self):
        return f"Comentario de {self.nombre_usuario} en '{self.articulo.titulo}'"
