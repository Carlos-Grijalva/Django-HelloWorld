from django.db import models

# Create your models here.
class Cargo(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Persona(models.Model):
    nombre = models.CharField(max_length=50)
    apellidoM = models.CharField(max_length=50)
    apellidoP = models.CharField(max_length=50)
    numero = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre
