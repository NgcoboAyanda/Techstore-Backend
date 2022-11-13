from django.db import models
from shop.models import Product

# Create your models here.
class Computer(Product):
    brand_name = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    processor = models.CharField(max_length=100)
    storage = models.IntegerField()#in MB
    memory = models.IntegerField()#in MB
    image = models.ImageField()

class Desktop(Computer):
    size = models.CharField(max_length=100)#e.g SFF

class Laptop(Computer):
    screen_resolution = models.CharField(max_length=100)
    battery_capacity = models.CharField(max_length=100)
    battery_life = models.IntegerField()#in hours