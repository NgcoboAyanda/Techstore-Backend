from rest_framework import serializers
from computers.models import Desktop, Laptop

#Desktop Serializer
class DesktopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Desktop
        fields = '__all__'

#Laptop Serializer
class LaptopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Laptop
        fields = '__all__'