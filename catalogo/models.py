from django.db import models

class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    biografia = models.TextField(blank=True, null=True, help_text="Biografía (opcional)")

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

    class Meta:
        verbose_name_plural = "Autores"

class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    ano_publicacion = models.IntegerField(verbose_name="Año de publicación")
    
    # Relación 1-N: Un Libro tiene un Autor
    autor = models.ForeignKey(
        Autor, 
        on_delete=models.CASCADE, 
        related_name='libros' # Permite acceder a autor.libros.all()
    )

    def __str__(self):
        return self.titulo