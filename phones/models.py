from django.db import models
from shop.models import Product

# Create your models here.
class Phone(Product):
    screen_size = models.CharField(max_length=10)
    battery = models.CharField(max_length=100)
    camera = models.CharField(max_length=50)
    os = models.CharField(max_length=50)
    ram = models.CharField(max_length=10)
    storage = models.CharField(max_length=10)