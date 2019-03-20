from rest_framework import serializers
from . import models


class ProductoSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'nombre', 'cantidad', 'valor', 'unidad', 'tipo',)
        model = models.Producto
