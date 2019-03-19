from django import forms
from .models import Variable, Producto

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = [
            'variable',
            'value',
            'unit',
            'place',
            #'dateTime',
        ]

        labels = {
            'variable' : 'Variable',
            'value' : 'Value',
            'unit' : 'Unit',
            'place' : 'Place',
            #'dateTime' : 'Date Time',
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
