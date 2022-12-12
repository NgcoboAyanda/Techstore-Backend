from django.urls import path
from rest_framework.generics import ListAPIView

from phones.models import Phone
from phones.serializers import PhoneSerializer

urlpatterns = [
    path('phones/', ListAPIView.as_view(queryset=Phone.objects.all(), serializer_class=PhoneSerializer), name='phone-list')
]
