from rest_framework import serializers

class UserSerializer(serializers.Serializer):
    email = serializers.EmailField()
    first_name = serializers.CharField(max_length=40)
    last_name = serializers.CharField(max_length=60)
    date_of_birth = serializers.DateField()