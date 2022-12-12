from django.db import models
from shop.models import Product

class Tablet(Product):
    screen_size = models.CharField(max_length=10)
    battery = models.CharField(max_length=100)
    camera = models.CharField(max_length=50)
    os = models.CharField(max_length=50)
    ram = models.CharField(max_length=10)
    storage = models.CharField(max_length=10)