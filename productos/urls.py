from django.urls import path
from django.conf.urls import url, include
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    path(r'', views.index,name='index'),
    path(r'base_layout',views.base_layout,name='base_layout'),
    path(r'getdata',views.getdata,name='getdata'),
    path(r'^productos/', views.ProductoList,name='productoList'),
    path(r'^productocreate/$', csrf_exempt(views.ProductoCreate), name='productoCreate'),
    path(r'^productoupdate/(?P<pk>\d+)/$', csrf_exempt(views.ProductoUpdate), name='productoUpdate'),
    path(r'^ventas/', views.VentaList),
    path(r'^ventacreate/$', csrf_exempt(views.VentaCreate), name='ventaCreate'),
]
