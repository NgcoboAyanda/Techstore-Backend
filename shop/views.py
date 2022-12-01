from rest_framework import viewsets
from rest_framework.response import Response
from .models import Product
from . import serializers

# Create your views here.
class GetAllProductsViewSet(viewsets.ViewSet):
    """ 
    Viewset for listing all products on the site.
    """
    def list(self, request):
        queryset = Product.objects.all()
        serializer = serializers.ProductSerializer(queryset, many=True)
        return Response(serializer.data)

class GetSpecificProductViewset(viewsets.ViewSet):
    """
    Viewset for getting a specific product by id.
    """
    def retrieve(self, request, pk=None):
        if pk:
            product = Product.objects.get(pk=pk)
            serializer = serializers.ProductSerializer(product)
            return Response(serializer.data)