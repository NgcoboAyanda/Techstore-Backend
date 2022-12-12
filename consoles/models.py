from django.db import models
from shop.models import Product

class Console(Product):
    color = models.CharField(max_length=50)
    storage = models.CharField(max_length=10)
