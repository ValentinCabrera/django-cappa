from rest_framework import serializers
from .models import ItemPedido, Pedido
from productos.serializers import ProductoSerializer

class ItemPedidoSerializer(serializers.ModelSerializer):
    producto = ProductoSerializer()

    class Meta:
        model = ItemPedido
        fields = '__all__'

class PedidoSerializer(serializers.ModelSerializer):
    items = serializers.SerializerMethodField()
    total = serializers.SerializerMethodField()

    class Meta:
        model = Pedido
        fields = '__all__'


    def get_total(self, obj):
        return obj.get_total()
    
    def get_items(self, obj):
        items = obj.items.order_by('orden')
        return ItemPedidoSerializer(items, many=True).data
