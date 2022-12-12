from rest_framework import serializers
from .models import Console


class ConsoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Console
        fields = ['__all__']