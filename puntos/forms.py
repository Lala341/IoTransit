from django import forms
from .models import Punto, Registro

class PuntoForm(forms.ModelForm):
    class Meta:
        model = Punto
        fields = [
            'id',
            'nombre',
            'direccion',
            'barrio',
            'ciudad',
            'tipo',


        ]

        labels = {

        'id' : 'Id',
        'nombre': 'Nombre',
        'direccion': 'Direccion',
        'barrio':'Barrio',
        'ciudad':'Ciudad',
        'tipo':'Tipo',


        }

class RegistroForm(forms.ModelForm):
    class Meta:
        model = Registro
        fields = [
            'punto',
            'cantidad',
        ]
        labels = {
            'punto': 'Punto',
            'cantidad': 'Cantidad',
        }
