from .models import Producto, Variable
from django.shortcuts import render, redirect
from .forms import VariableForm, ProductoForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse


def index(request):
    return render(request, 'index.html')

def ProductoList(request):
    queryset = Producto.objects.all().order_by('-dateTime')[:10]
    context = {
        'producto_list': queryset
    }
    return render(request, 'Producto/productos.html', context)

def ProductoCreate(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            producto = form.save()
            producto.save()
            messages.add_message(request, messages.SUCCESS, 'Producto create successful')
            return HttpResponseRedirect(reverse('productoCreate'))
        else:
            print(form.errors)
    else:
        form = ProductoForm()

    context = {
        'form': form,
    }

    return render(request, 'Producto/productoCreate.html', context)

def VariableList(request):
    queryset = Variable.objects.all()
    context = {
        'variable_list': queryset
    }
    return render(request, 'Variable/variables.html', context)

def VariableCreate(request):
    if request.method == 'POST':
        form = VariableForm(request.POST)
        if form.is_valid():
            producto = form.save()
            producto.save()
            messages.add_message(request, messages.SUCCESS, 'Variable create successful')
            return HttpResponseRedirect(reverse('variableCreate'))
        else:
            print(form.errors)
    else:
        form = VariableForm()

    context = {
        'form': form,
    }

    return render(request, 'Variable/variableCreate.html', context)
