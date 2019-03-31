from django.db import models

# Create your models here.

class Punto(models.Model):
    nombre = models.CharField(max_length=100, default='DEFAULT VALUE')
    direccion = models.CharField(max_length=100, default='DEFAULT VALUE')
    barrio = models.CharField(max_length=50, default='DEFAULT VALUE')
    ciudad = models.CharField(max_length=50, default='DEFAULT VALUE')
    tipo = models.CharField(max_length=50, default='DEFAULT VALUE')

    def __str__(self):
        return '%s %s' % (self.nombre, self.tipo)

class Registro(models.Model):
    punto = models.ForeignKey(Punto, on_delete=models.CASCADE)
    cantidad = models.FloatField(null=True, blank=True)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'El registro fue del punto: $'.format(self.punto)
