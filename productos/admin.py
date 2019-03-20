from django.contrib import admin
from . models import Producto, Variable, Venta

# Register your models here.
admin.site.register(Producto)
admin.site.register(Venta)
admin.site.register(Variable)
