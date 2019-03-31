from .models import Punto, Registro
from django.shortcuts import render, redirect
from .forms import  PuntoForm, RegistroForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core import serializers
from django.http import HttpResponse
import json
# Create your views here.

def index(request):
    template='index.html'
    registros= Registro.objects.all()
    jsondata = serializers.serialize('json',registros)
    context={
		'results':results,
		'jsondata':jsondata,
	}
    return render(request,template,context)

def puntos(request):
	template='Punto/puntos.html'
	results=Punto.objects.all()
	jsondata = serializers.serialize('json',results)
	context={
		'results':results,
		'jsondata':jsondata,
	}
	return render(request,template,context)

def getdata(request):

    registros= Registro.objects.all()
    jsondata = serializers.serialize('json',registros)
    return HttpResponse(jsondata)

def base_layout(request):
	template='base.html'
	return render(request,template)

def PuntoList(request):
    queryset = Punto.objects.all()
    context = {
        'punto_list': queryset
    }
    return render(request, 'Punto/puntos.html', context)

def PuntoCreate(request):
    if request.method == 'POST':
        form = PuntoForm(request.POST)
        if form.is_valid():
            punto = form.save()
            punto.save()
            messages.add_message(request, messages.SUCCESS, 'Punto create successful')
            return HttpResponseRedirect(reverse('puntoList'))
        else:
            print(form.errors)
    else:
        form = PuntoForm()

    context = {
        'form': form,
    }

    return render(request, 'Punto/puntoCreate.html', context)

def PuntoUpdate(request,pk):
    punto= Punto.objects.get(id=pk)
    if request.method == 'GET':
        form= PuntoForm(instance=punto)
    else:
        form= PuntoForm(request.POST, instance=punto)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Punto update successful')
            return HttpResponseRedirect(reverse('puntoList'))

    context = {
        'form': form,
    }

    return render(request, 'Punto/puntoUpdate.html', context)

def RegistroList(request):
    queryset = Registro.objects.all()
    context = {
        'registro_list': queryset
    }
    return render(request, 'Registro/registros.html', context)

def RegistroCreate(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            registro = form.save()
            registro.save()
            messages.add_message(request, messages.SUCCESS, 'Registro create successful')
            return HttpResponseRedirect(reverse('registroCreate'))
        else:
            print(form.errors)
    else:
        form = RegistroForm()

    context = {
        'form': form,
    }

    return render(request, 'Registro/registroCreate.html', context)
