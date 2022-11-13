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

    paginate_by = 20

    def createResponse(self, category_name, no_of_products, items, current_page_no, last_page_no):
        return {
            'category_name': category_name,
            'products': {
                'total_number_of_products': no_of_products,
                'items': items
            },
            'current_page_number': current_page_no,
            'last_page_number': last_page_no
        }

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
        print(data)


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