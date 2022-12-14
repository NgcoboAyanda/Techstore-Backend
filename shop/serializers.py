from rest_framework import serializers
from .models import Product
from computers.models import Laptop, Desktop
from computers.serializers import LaptopSerializer, DesktopSerializer

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'