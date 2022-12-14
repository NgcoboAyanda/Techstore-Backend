from rest_framework import serializers
from . import models

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MyUser
        fields = ['email', 'first_name', 'last_name', 'uid', 'phone']