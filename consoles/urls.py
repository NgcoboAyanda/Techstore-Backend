from django.urls import path
from rest_framework.generics import ListAPIView

from .models import Console
from .serializers import ConsoleSerializer

urlpatterns = [
    path('accessories/', ListAPIView.as_view(queryset=Console.objects.all(), serializer_class=ConsoleSerializer), name='list-accessories')
]
