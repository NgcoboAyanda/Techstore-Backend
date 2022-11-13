from django.db import models
from shop.models import Product

# Create your models here.
class Computer(Product):
    brand_name = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    processor = models.CharField(max_length=100)
    STORAGE_CHOICES = (
        ('Small', 256),
        ('Medium', 512),
        ('Large', 1024),
        ('Extreme', 2048)
    )
    storage = models.IntegerField(choices=STORAGE_CHOICES)#in GB
    MEMORY_CHOICES = (
        ('Small', 4),
        ('Medium', 8),
        ('Large', 16),
        ('Extreme', 32)
    )
    memory = models.IntegerField(choices=MEMORY_CHOICES)#in GB
    image = models.ImageField()

class Desktop(Computer):
    COMPUTER_CASE_SIZE_CHOICES = (
        ('Small', "SFF"),
        ('Mini', "Mini Tower")
        ('Mid', "Mid Tower"),
        ('Big', "Full Tower")
    )
    size = models.CharField(max_length=100, choices=COMPUTER_CASE_SIZE_CHOICES)#e.g SFF

class Laptop(Computer):
    SCREEN_RESOLUTION_CHOICES = (
        ('WXGA', "1280x800"),
        ('HD', "1366x768"),
        ('HD+', "1600x900"),
        ('FHD', "1920x1080"),
        ('QHD', "2560x1440"),
        ('QHD+', "3200x1800"),
        ('UHD', "3840x2160")
    )
    screen_resolution = models.CharField(max_length=100, choices=SCREEN_RESOLUTION_CHOICES)
    battery_capacity = models.CharField(max_length=100)#in mAH
    battery_life = models.IntegerField()#in hours