from django.db import models
from django.utils import timezone
# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=255)
    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=255)
    stock = models.IntegerField()
    puntaje = models.FloatField()
    #CASCADE: elimina el prod
    #PROCTECT: lanza error
    #RESTRICT: solo elimina si no existe producto
    #SET_NULL: actualiza a null
    #SET_DEFAULT: asigna valor por defecto
    categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE)
    creado_en = models.DateTimeField(default = timezone.now)
    def __str__(self):
        return self.nombre
