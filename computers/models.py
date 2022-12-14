from django.db import models
from shop.models import Product

class Desktop(Product):
    category = "desktop"
    size = models.CharField(max_length=100)#e.g SFF
    os = models.CharField(max_length=50, default="Windows 10")
    ram = models.CharField(max_length=10, default="8GB")
    storage = models.CharField(max_length=10, default="512GB SSD")
    gpu = models.CharField(max_length=100, default="Integrated Graphics")


class Laptop(Product):
    category = "laptop"
    battery = models.CharField(max_length=100, default="5000mAh")
    camera = models.CharField(max_length=50, default="720p")
    os = models.CharField(max_length=50, default="Windows 10")
    ram = models.CharField(max_length=10, default="8GB")
    storage = models.CharField(max_length=10, default="512GB SSD")
    gpu = models.CharField(max_length=100, default="Integrated Graphics")
    