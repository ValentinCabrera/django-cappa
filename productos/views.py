from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ProductoSerializer, CategoriaSerializer, ProductosPedidosSerializer
from .models import Producto, Categoria

from pedidos.models import Pedido

class ProductosListView(APIView):
    def get(self, request, categoria_id=None):
        if categoria_id:
            productos = Producto.objects.filter(categoria__id=categoria_id)
        
        else:
            productos = Producto.objects.all()
        serializer = ProductoSerializer(productos, many=True)
        return Response(serializer.data)

class ProductosPedidosListView(APIView):
    def post(self, request):
        pedido_id = request.data.get("pedido")
        categoria = request.data.get("categoria")

        productos = Producto.objects.filter(categoria__id=categoria)
        serializer = ProductosPedidosSerializer(productos, many=True, context={'pedido_id': pedido_id})
        return Response(serializer.data)


class ProductoListView(APIView):
    def get(self, request, pk=None):
        if pk:
            producto = Producto.objects.get(id=pk)
            serializer = ProductoSerializer(producto)

            return Response(serializer.data)
        
        productos = Producto.objects.all()
        serializer = ProductoSerializer(productos, many=True)
        return Response(serializer.data)
    
class CategoriasListView(APIView):
    def get(self, request, pk=None):
        if pk:
            categoria = Categoria.objects.get(id=pk)
            serializer = CategoriaSerializer(categoria)

            return Response(serializer.data)
        
        else:
            categorias = Categoria.objects.all()
            serializer = CategoriaSerializer(categorias, many=True)

            return Response(serializer.data)
