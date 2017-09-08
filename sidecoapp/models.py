from django.db import models
from django.utils import timezone

class Desempleado(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    fecha_nacimiento = models.DateField()
    tipo_trabajo = models.CharField(max_length=50)
    dni = models.IntegerField()

    def __str__(self):
        return self.nombre

class Empresa(models.Model):
    cuil = models.IntegerField()
    razon_social = models.CharField(max_length=50)
    rubro = models.CharField(max_length=30)
    oferta_laboral = models.ForeignKey('OfertaLaboral')

    def __str__(self):
        return self.razon_social

class OfertaLaboral(models.Model):
    empresa_oferta = models.ForeignKey('Empresa')
    trabajo_solicitado = models.CharField(max_length=50)