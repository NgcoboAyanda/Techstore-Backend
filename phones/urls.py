from django.urls import path
from rest_framework.generics import ListAPIView, RetrieveAPIView

from phones.models import Phone
from phones.serializers import PhoneSerializer

urlpatterns = [
    path('phones/', ListAPIView.as_view(queryset=Phone.objects.all(), serializer_class=PhoneSerializer), name='list-phones'),
    path('phones/<int:pk>/', RetrieveAPIView.as_view(queryset=Phone.objects.all(), serializer_class=PhoneSerializer), name='get-single-phone')
]
