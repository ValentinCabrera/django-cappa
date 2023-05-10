from django.contrib import admin
from .models import Pedido, ItemPedido

class PedidoAdmin(admin.ModelAdmin):
    readonly_fields = ('get_total',)
    list_display = ('id', 'fecha', 'estado', 'get_total')

class ItemPedidoAdmin(admin.ModelAdmin):
    list_display = ('id', 'pedido', 'producto', 'cantidad')

admin.site.register(Pedido, PedidoAdmin)
admin.site.register(ItemPedido, ItemPedidoAdmin)