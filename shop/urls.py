from django.urls import path
from rest_framework.generics import ListAPIView

from .models import Product
from .serializers import ProductSerializer

urlpatterns = [
    path('all/', ListAPIView.as_view(queryset=Product.objects.all(), serializer_class=ProductSerializer))
]
