from rest_framework import viewsets
from rest_framework.response import Response


# Create your views here.
class DesktopsViewset(viewsets.ViewSet):
    """
    A simple view for listing or retrieving desktop computers.
    """
    def list(self, request):
        pass


class LaptopsViewset(viewset.ViewSet):
    """
    A simple view for listing or retrieving laptop computers.
    """
    def list(self, request):
        pass