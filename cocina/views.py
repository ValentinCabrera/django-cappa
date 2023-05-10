from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import CocinaSerializer
from pedidos.models import Pedido
from rest_framework import status

class CocinaAPIView(APIView):
    def get(self, request):
        pedidos = Pedido.objects.filter(estado=2)
        pedidos = pedidos.order_by('fecha')
        serializer = CocinaSerializer(pedidos, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        pk = request.data.get("pedido")
        estado = request.data.get("estado")
        pedido = Pedido.objects.get(pk=pk)
        pedido.estado = estado
        pedido.save()

        return(Response(status=status.HTTP_202_ACCEPTED))