from django.contrib import admin
from .models import Producto , Carrito, CarritoProducto

admin.site.register(Producto)
admin.site.register(CarritoProducto)
admin.site.register(Carrito)

