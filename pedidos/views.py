from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ItemPedido, Pedido
from productos.models import Producto
from .serializers import ItemPedidoSerializer, PedidoSerializer
from django.shortcuts import get_object_or_404
from django.utils import timezone
from cocina.serializers import CocinaSerializer

class PedidosEstadosAPIView(APIView):
    def get(self, request, pk=None):
        if pk:
            pedidos = Pedido.objects.filter(estado = pk)
            serializer = PedidoSerializer(pedidos, many=True)

            return Response(serializer.data)

class PedidoAPIView(APIView):
    def get(self, request, pk=None, productoId=None):
        if pk:
            pedido = get_object_or_404(Pedido, pk=pk)
            serializer = PedidoSerializer(pedido)

            if productoId:
                cantidad = 0
                try:
                    item = ItemPedido.objects.get(pedido=pedido, producto=productoId)
                    cantidad = item.cantidad
                except ItemPedido.DoesNotExist:
                    pass                  
                return Response({'cantidad': cantidad, 'total': serializer.data['total']})
            else:
                items = pedido.items.order_by('orden')
                data = serializer.data
                data['items'] = ItemPedidoSerializer(items, many=True).data
                return Response(data)
        else:
            pedidos = Pedido.objects.all()
            serializer = PedidoSerializer(pedidos, many=True)
            return Response(serializer.data)

    def post(self, request):
        pedido = Pedido()
        pedido.save()
        
        serializer = PedidoSerializer(pedido)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def patch(self, request, pk=None):
        if pk:
            pedido = get_object_or_404(Pedido, pk=pk)

        state = request.data.get('state')

        pedido.estado = state
        pedido.fecha = timezone.now()
        pedido.save()
        return Response({'error': 'Pedido realizado'}, status=status.HTTP_100_CONTINUE)

class ItemPedidoAPIView(APIView):
    def get(self, request, pk):
        if pk: 
            item = get_object_or_404(ItemPedido, id=pk)
            serializer = ItemPedidoSerializer(item)

            return Response(serializer.data)
        
        return Response({'error':'El item no existe'})


    def post(self, request):
        producto = get_object_or_404(Producto, pk=request.data.get("producto"))
        pedido = get_object_or_404(Pedido, pk=request.data.get("pedido"))

        if not producto:
            return Response({'error': 'El producto es requerido'}, status=status.HTTP_400_BAD_REQUEST)

        if not pedido:
            return Response({'error': 'El pedido es requerido'}, status=status.HTTP_400_BAD_REQUEST)

        item = ItemPedido(producto=producto, pedido=pedido)
        item.save()

        serializer = PedidoSerializer(pedido)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def patch(self, request):
        producto = get_object_or_404(Producto, pk=request.data.get("producto"))
        pedido = get_object_or_404(Pedido, pk=request.data.get("pedido"))

        item = ItemPedido.objects.get(pedido=pedido, producto=producto)
        accion = request.data.get('accion')

        if accion == '+':
            item.aumentar_cantidad()

        elif accion == '-':
            item.disminuir_cantidad()

        elif accion == 'delete':
            item.delete()

        else:
            return Response({'error': 'Acción no válida.'}, status=status.HTTP_400_BAD_REQUEST)
        
        serializer = PedidoSerializer(pedido)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
class SalonPedidosAPIView(APIView):
    def get(self, request):
        pedidos = Pedido.objects.filter(estado=3)
        pedidos = pedidos.order_by('fecha')
        serializer = CocinaSerializer(pedidos, many=True)
        return Response(serializer.data)