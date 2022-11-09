from django.urls import include, path
from computers.views import DesktopsViewset, LaptopsViewset
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'desktops', DesktopsViewset, basename="desktops")
router.register(r'laptops', LaptopsViewset, basename="laptops")

