from django.urls import path
from rest_framework.generics import ListAPIView, RetrieveAPIView

from .models import Tablet
from .serializers import TabletSerializer

urlpatterns = [
    path('tablets/', ListAPIView.as_view(queryset=Tablet.objects.all(), serializer_class=TabletSerializer), name='list-tablets' ),
    path('tablets/<int:pk>/', RetrieveAPIView.as_view(queryset=Tablet.objects.all(), serializer_class=TabletSerializer), name='get-single-tablet')
]

