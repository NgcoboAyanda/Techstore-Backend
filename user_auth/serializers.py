from rest_framework import serializers
from . import models

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MyUser
        fields = ['email', 'first_name', 'last_name', 'date_of_birth', 'uid', 'phone']

class OTPSerializer(serializers.Serializer):
    class Meta:
        model = models.OTP
        fields = '__all__'