from rest_framework import viewsets
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
import json

from computers.models import Laptop, Desktop
from computers.serializers import LaptopSerializer, DesktopSerializer

# Create your views here.
class DesktopsViewset(viewsets.GenericViewSet):
    """
    A simple view for listing or retrieving desktop computers.
    """

    authentication_clases = [ TokenAuthentication ]
    permission_classes = [ IsAuthenticated ]

    def list(self, request):
        queryset = Desktop.objects.all()
        serializer = DesktopSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        pass


    def retrieve(self, request, pk=None):
        queryset = Desktop.objects.all()
        if pk:
            computer = Desktop.objects.get(pk=pk)
            serializer = DesktopSerializer(queryset)
            return Response(serializer.data)



class LaptopsViewset(viewsets.GenericViewSet):
    """
    A simple view for listing or retrieving laptop computers.
    """

    authentication_clases = [ TokenAuthentication ]
    permission_classes = [ IsAuthenticated ]

    def list(self, request):
        pass

    def create(self, request, *args, **kwargs):
        serializer = LaptopSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(None, status=status.HTTP_201_CREATED)
        