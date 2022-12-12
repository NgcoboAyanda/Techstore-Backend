from django.urls import path
from rest_framework.generics import ListAPIView

from .models import Accessory
from .serializers import AccessorySerializer

urlpatterns = [
    path('accessories/', ListAPIView.as_view(queryset=Accessory.objects.all(), serializer_class=AccessorySerializer), name='list-accessories')
]


