from django.db import models
from .managers import AutorManager
class Autor(models.Model):
    nombre = models.CharField(
        max_length=50
    )
    apellidos = models.CharField(
        max_length=50
    )
    nacionalidad = models.CharField(
        max_length=30
    )
    edad = models.PositiveIntegerField()
    # Al instanciar AutorManager() conectamos la clase Autor con AutorManager()
    objects = AutorManager()
    
    def __str__(self):
        return self.nombre + "-" + self.apellidos
