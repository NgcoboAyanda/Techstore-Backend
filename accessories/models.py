from django.db import models
from shop.models import Product

class Accessory(Product):
    color = models.CharField(max_length=50)
    connectivity = models.CharField(max_length=100)
    battery_life = models.CharField(max_length=100)
    water_resistance = models.CharField(max_length=100, default="None")
