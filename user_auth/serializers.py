from rest_framework import serializers
from .models import MyUser

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = MyUser
        fields = ['email', 'first_name', 'last_name', 'date_of_birth', 'uid', 'phone']