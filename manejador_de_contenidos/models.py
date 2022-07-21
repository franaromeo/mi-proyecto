from unittest.util import _MAX_LENGTH
from django.db import models

class Curso(models.Model):

    nombre = models.CharField(max_length=40)
    camada = models.IntegerField()
    def __str__(self):
        return self.nombre

class Familiar(models.Model):

    nombre = models.CharField(max_length=40)
    edad = models.IntegerField()

class Estudiante(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()

class CursoFormulario(models.Model):

    nombre = models.CharField(max_length=40)
    camada = models.IntegerField()
    