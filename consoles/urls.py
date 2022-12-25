from django.urls import path
from rest_framework.generics import ListAPIView, RetrieveAPIView

from .models import Console
from .serializers import ConsoleSerializer

urlpatterns = [
    path('consoles/', ListAPIView.as_view(queryset=Console.objects.all(), serializer_class=ConsoleSerializer), name='list-consoles'),
    path('consoles/<int:pk>/', RetrieveAPIView.as_view(queryset=Console.objects.all(), serializer_class=ConsoleSerializer), name='get-single-console' )
]
