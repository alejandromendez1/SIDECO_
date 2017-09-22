from django.db import models
from django.utils import timezone

class Sistema(models.Model):
    empresas_verificadas = models.ForeignKey('Empresa', related_name='empresas_verificadas')
    desocupados_verificados = models.ForeignKey('Desocupado')
    empresas_en_alta = models.ForeignKey('Empresa', related_name='empresas_en_alta')

class Desocupado(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    fecha_nacimiento = models.DateField()
    localidad = models.CharField(max_length=20)
    estado_ocupacion = models.BooleanField()
    experiencia_laboral = models.TextField()
    formacion = models.TextField()
    habilidades = models.TextField()
    trabajo_realizable = models.CharField(max_length=50)
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
    tipo_de_trabajo = models.CharField(max_length=50)