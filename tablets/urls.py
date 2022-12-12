from django.urls import path
from rest_framework.generics import ListAPIView

from tablets.models import Tablet
from tablets.serializers import TabletSerializer

urlpatterns = [
    path('tablets/', ListAPIView.as_view(queryset=Tablet.objects.all, serializer_class=TabletSerializer), name='tablet-list' )
]

