from django.db import models

#Base Product Model
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    price = models.DecimalField(decimal_places=2, max_digits=11)
    stock = models.IntegerField()