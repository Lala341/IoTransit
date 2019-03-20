from django.db import models

# Create your models here.

class Variable(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return '{}'.format(self.name)

class Producto(models.Model):
    nombre = models.TextField()
    cantidad = models.FloatField(null=True, blank=True, default=None)
    valor = models.FloatField(null=True, blank=True, default=None)
    unidad = models.CharField(max_length=50, default="gramos")
    tipo = models.CharField(max_length=50, default="ABARROTES")

    def __str__(self):
        return '%s %s' % (self.nombre, self.tipo)
