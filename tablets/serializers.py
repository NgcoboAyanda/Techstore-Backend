from rest_framework import serializers
from tablets.models import Tablet

class TabletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tablet
        fields = ['__all__']