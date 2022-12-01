from django.db import models
from shop.models import Product

class Desktop(Product):
    size = models.CharField(max_length=100)#e.g SFF

class Laptop(Product):
    battery = models.CharField(max_length=100)
    camera = models.CharField(max_length=50)
    os = models.CharField(max_length=50)
    memory = models.CharField(max_length=50)