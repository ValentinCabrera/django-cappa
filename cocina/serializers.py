from rest_framework import serializers
from pedidos.models import Pedido, ItemPedido
from productos.models import Producto

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ['nombre']

class ItemSerializer(serializers.ModelSerializer):
    producto = serializers.CharField(source='producto.nombre')

    class Meta:
        model = ItemPedido
        fields = ['producto', 'cantidad']

class CocinaSerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True, source='items.all')
    color = serializers.SerializerMethodField()

    class Meta:
        model = Pedido
        fields = ['id', 'color', 'items']

    def get_color(self, obj):
        return obj.get_color()
