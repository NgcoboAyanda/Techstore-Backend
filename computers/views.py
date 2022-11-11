from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from computers.models import Laptop, Desktop
from computers.serializers import LaptopSerializer, DesktopSerializer

# Create your views here.
class DesktopsViewset(viewsets.ViewSet):
    """
    A simple view for listing or retrieving desktop computers.
    """
    authentication_clases = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def list(self, request):
        queryset = Desktop.objects.all()
        serializer = DesktopSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Desktop.objects.all()
        if pk:
            computer = Desktop.objects.get(pk=pk)
            serializer = DesktopSerializer(queryset)
            return Response(serializer.data)



class LaptopsViewset(viewsets.ViewSet):
    """
    A simple view for listing or retrieving laptop computers.
    """
    def list(self, request):
        pass