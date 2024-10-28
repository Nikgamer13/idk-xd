from django.contrib import admin
from .models import Producto, Pedido


# Registro básico

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio')

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('id', 'usuario', 'estado')
    list_filter = ('estado',)
    search_fields = ('usuario__username',)

