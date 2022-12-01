from rest_framework import serializers
from computers.models import Desktop, Laptop

#Desktop Serializer
class DesktopSerializer(serializers.ModelSerializer):
    size = serializers.CharField(max_length=100)

    class Meta:
        model = Desktop
        fields = ['name', 'description', 'price', 'stock', 'size']

#Laptop Serializer
class LaptopSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=100)
    description = serializers.CharField(max_length=1000)
    price = serializers.CharField(max_length=100)
    stock = serializers.IntegerField(default=20)
    battery = serializers.CharField(max_length=100)
    camera = serializers.CharField(max_length=50)
    os = serializers.CharField(max_length=50)
    memory = serializers.CharField(max_length=50)

    class Meta:
        model = Laptop
        fields = ['name', 'description', 'price', 'stock', 'battery', 'camera', 'os', 'memory']