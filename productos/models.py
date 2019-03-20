from django.db import models

# Create your models here.

class Variable(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return '{}'.format(self.name)

class Producto(models.Model):
    nombre = models.CharField(max_length=100, default='DEFAULT VALUE')
    cantidad = models.FloatField(null=True, blank=True, default=None)
    valor = models.FloatField(null=True, blank=True, default=None)
    unidad = models.CharField(max_length=50, default='DEFAULT VALUE')
    tipo = models.CharField(max_length=50, default='DEFAULT VALUE')

    def __str__(self):
        return '%s %s' % (self.nombre, self.tipo)

class Venta(models.Model):
    id = models.FloatField(null=True, blank=True, default=None)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    dateTime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'La venta $ fue con el producto: $'.format(self.id, self.producto)
