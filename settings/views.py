from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Setting
from .serializers import SettingSerializer

class SettingsAPIView(APIView):
    def get(self, request):
        setting = Setting.objects.get(id=1)
        serializer = SettingSerializer(setting)

        return Response(serializer.data)
