from rest_framework import serializers
from . import models


class PuntoSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'nombre', 'direccion', 'barrio', 'ciudad', 'tipo',)
        model = models.Punto
