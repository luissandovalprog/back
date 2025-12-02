from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    
    class Roles(models.TextChoices):
        BIBLIOTECARIO = 'Bibliotecario', 'Bibliotecario'
        LECTOR = 'Lector', 'Lector'

    # El rol por defecto será 'Lector'
    rol = models.CharField(
        max_length=20,
        choices=Roles.choices,
        default=Roles.LECTOR
    )

    def __str__(self):
        return self.username