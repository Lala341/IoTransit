from django.urls import path
from django.conf.urls import url, include
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    url(r'^$', views.index,name='index'),
    url(r'base_layout',views.base_layout,name='base_layout'),
    url(r'getdata',views.getdata,name='getdata'),

    url(r'^puntos/', views.PuntoList,name='puntoList'),
    url(r'^puntocreate/$', csrf_exempt(views.PuntoCreate), name='puntoCreate'),
    url(r'^puntooupdate/(?P<pk>\d+)/$', csrf_exempt(views.PuntoUpdate), name='puntoUpdate'),
    url(r'^registros/', views.RegistroList, name='registroList'),
    url(r'^registrocreate/$', csrf_exempt(views.RegistroCreate), name='registroCreate'),
]
