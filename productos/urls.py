from django.urls import path
from django.conf.urls import url, include
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    url('^$', views.index),
    url(r'^productos/', views.ProductoList),
    url(r'^productocreate/$', csrf_exempt(views.ProductoCreate), name='productoCreate'),
    url(r'^productoupdate/(?P<pk>\d+)/$', csrf_exempt(views.ProductoUpdate), name='ProductoUpdate'),
    url(r'^ventas/', views.VentaList),
    url(r'^ventacreate/$', csrf_exempt(views.VentaCreate), name='ventaCreate'),
    url(r'^variables/', views.VariableList, name='variableList'),
    url(r'^variablecreate/$', csrf_exempt(views.VariableCreate), name='variableCreate'),
]
