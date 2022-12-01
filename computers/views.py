from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from computers.models import Laptop, Desktop
from computers.serializers import LaptopSerializer, DesktopSerializer

class ComputersViewSet(mixins.ListModelMixin,viewsets.GenericViewSet):
    """
    The base viewset for all computer categories
    """
    
    authentication_clases = [ TokenAuthentication ]
    permission_classes = [ IsAuthenticated ]

# Create your views here.
class DesktopsViewset(ComputersViewSet):
    """
    A simple view for listing or retrieving desktop computers.
    """

    category_name = "desktops"

    def list(self, request):
        queryset = Desktop.objects.all()
        serializer = DesktopSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, data):
        pass


    def retrieve(self, request, pk=None):
        queryset = Desktop.objects.all()
        if pk:
            computer = Desktop.objects.get(pk=pk)
            serializer = DesktopSerializer(queryset)
            return Response(serializer.data)



class LaptopsViewset(ComputersViewSet):
    """
    A simple view for listing or retrieving laptop computers.
    """

    category_name = "laptops"

    def list(self, request):
        pass

    def create(self, data):
        pass