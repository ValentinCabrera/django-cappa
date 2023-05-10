from rest_framework import serializers
from .models import Producto, Categoria
from pedidos.models import Pedido

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

class ProductoSerializer(serializers.ModelSerializer):
    categoria = CategoriaSerializer(read_only=True)
    class Meta:
        model = Producto
        fields = '__all__'


class ProductosPedidosSerializer(serializers.ModelSerializer):
    cantidad_seleccionada = serializers.SerializerMethodField()

    class Meta:
        model = Producto
        fields = ['id', 'imagen','nombre', 'precio', 'cantidad_seleccionada']

    def get_cantidad_seleccionada(self, obj):
        pedido_id = self.context.get('pedido_id')
        if not pedido_id:
            return 0
        
        pedido = Pedido.objects.get(pk=pedido_id)
        item = pedido.items.filter(producto=obj).first()
        if item:
            return item.cantidad
        else:
            return 0
