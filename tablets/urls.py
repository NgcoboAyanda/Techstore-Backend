from django.urls import path
from rest_framework.generics import ListAPIView

from .models import Tablet
from .serializers import TabletSerializer

urlpatterns = [
    path('tablets/', ListAPIView.as_view(queryset=Tablet.objects.all(), serializer_class=TabletSerializer), name='tablet-list' )
]

