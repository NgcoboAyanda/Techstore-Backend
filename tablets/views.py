from django.shortcuts import render
from rest_framework import views

from tablets.models import Tablet
from tablets.serializers import TabletSerializer
# Create your views here.
class TabletView(views.GenericView):
    queryset = Tablet.objects.all()
    serializer = TabletSerializer