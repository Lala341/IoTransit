from django.db import models

# Create your models here.

class Variable(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return '{}'.format(self.name)

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    cantidad = models.FloatField(null=True, blank=True, default=None)
    valor = models.FloatField(null=True, blank=True, default=None)
    unidad = models.CharField(max_length=50)
    tipo = models.CharField(max_length=50)

    def __str__(self):
        return '%s %s' % (self.value, self.unit)
