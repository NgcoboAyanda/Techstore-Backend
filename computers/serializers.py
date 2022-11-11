from rest_framework import serializers
from computers.models import Desktop, Laptop

class DesktopSerializer(serializers.Serializer):
    class Meta:
        model = Desktop
        fields = ["__all__"]

class LaptopSerializer(serializers.Serializer):
    class Meta:
        model = Laptop
        fields = ["__all__"]
