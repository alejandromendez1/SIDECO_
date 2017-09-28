from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Sistema(models.Model):
    empresas_verificadas = models.ForeignKey('Empresa', related_name='empresas_verificadas')
    desocupados_verificados = models.ForeignKey('Desocupado')
    empresas_en_alta = models.ForeignKey('Empresa', related_name='empresas_en_alta')

class Desocupado(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    fecha_nacimiento = models.DateField()
    localidad = models.CharField(max_length=20)
    estado_ocupacion = models.BooleanField()
    experiencia_laboral = models.TextField()
    formacion = models.TextField()
    habilidades = models.TextField()
    trabajo_realizable = models.CharField(max_length=50)
    dni = models.CharField(max_length=10)
    email = models.EmailField(max_length=25)

@receiver(post_save, sender=User)
def update_user_desocupado(sender, instance, created, **kwargs):
    if created:
        Desocupado.objects.create(user=instance)
        instance.desocupado.save()

class Empresa(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cuil = models.IntegerField()
    razon_social = models.CharField(max_length=50)
    rubro = models.CharField(max_length=30)
    oferta_laboral = models.ForeignKey('OfertaLaboral')

    def __str__(self):
        return self.razon_social

@receiver(post_save, sender=User)
def update_user_empresa(sender, instance, created, **kwargs):
    if created:
        Empresa.objects.create(user=instance)
        instance.empresa.save()
        
class OfertaLaboral(models.Model):
    empresa_oferta = models.ForeignKey('Empresa')
    tipo_de_trabajo = models.CharField(max_length=50)
