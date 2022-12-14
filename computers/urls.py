from django.urls import path
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from computers.views import DesktopsViewset, LaptopsViewset
from rest_framework.routers import DefaultRouter

from .models import Desktop, Laptop
from .serializers import DesktopSerializer, LaptopSerializer
#router = DefaultRouter()
#router.register(r'desktops', DesktopsViewset, basename="desktops")
#router.register(r'laptops', LaptopsViewset, basename="laptops")
#urlpatterns = router.urls

urlpatterns = [
    path('desktops/', ListCreateAPIView.as_view(queryset=Desktop.objects.all(), serializer_class=DesktopSerializer), name='list-desktops'),
    path('desktops/<int:pk>/', RetrieveAPIView.as_view(queryset=Desktop.objects.all(), serializer_class=DesktopSerializer), name="get-single-desktop")
    ,

    path('laptops/', ListCreateAPIView.as_view(queryset=Laptop.objects.all(), serializer_class=LaptopSerializer), name='list-laptops'),
    path('laptops/<int:pk>/', RetrieveAPIView.as_view(queryset=Laptop.objects.all(), serializer_class=LaptopSerializer, lookup_field="pk"), name='get-single-laptop')
]
