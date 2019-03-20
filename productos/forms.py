from django import forms
from .models import Variable, Producto

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = [
            'id',
            'nombre',
            'cantidad',
            'valor',
            'unidad',
            'tipo',


        ]

        labels = {

        'id' : 'Id',
        'nombre': 'Nombre',
        'cantidad': 'Cantidad',
        'valor':'Valor',
        'unidad':'Unidad',
        'tipo':'Tipo',


        }

class VariableForm(forms.ModelForm):
    class Meta:
        model = Variable
        fields = [
            'name',
        ]
        labels = {
            'name': 'Name',
        }
