from .models import Producto, Venta, Variable
from django.shortcuts import render, redirect
from .forms import VariableForm, ProductoForm, VentaForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse


def index(request):
    return render(request, 'index.html')

def ProductoList(request):
    queryset = Producto.objects.all()
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

def ProductoUpdate(request,pk):
    prodbus= Producto.objects.get(id=pk)
    if request.method == 'GET':
        form= ProductoForm(instance=prodbus)
    else:
        form= ProductoForm(request.POST, instance=prodbus)
        if form.is_valid():
            form.save()
            
            messages.add_message(request, messages.SUCCESS, 'Producto update successful')
            return HttpResponseRedirect(reverse('productoUpdate'))
        else:
            print(form.errors)

    context = {
        'form': form,
    }

    return render(request, 'Producto/productoUpdate.html', context)

def VentaList(request):
    queryset = Venta.objects.all().order_by('-dateTime')[:10]
    context = {
        'venta_list': queryset
    }
    return render(request, 'Venta/ventas.html', context)

def VentaCreate(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            venta = form.save()
            venta.save()
            messages.add_message(request, messages.SUCCESS, 'Venta creada con exito')
            return HttpResponseRedirect(reverse('ventaCreate'))
        else:
            print(form.errors)
    else:
        form = VentaForm()

    context = {
        'form': form,
    }

    return render(request, 'Venta/ventaCreate.html', context)

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
