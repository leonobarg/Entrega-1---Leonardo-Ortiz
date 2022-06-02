from operator import mod
from django.db import models

# Create your models here.
class Paciente(models.Model):
    apellido=models.CharField(max_length=40)
    nombre=models.CharField(max_length=40)
    dni=models.IntegerField()
    fechaNac=models.DateField()
    obraSocial=models.CharField(max_length=40)
    afiliado=models.CharField(max_length=20)
    email=models.EmailField()

class Medico(models.Model):
    profesional=models.CharField(max_length=40)
    mp=models.IntegerField()
    especialidad=models.CharField(max_length=40)

class Obrasocial(models.Model):
    nombre=models.CharField(max_length=40)
    direccion=models.CharField(max_length=40)
    email=models.EmailField()
    cuit=models.IntegerField()