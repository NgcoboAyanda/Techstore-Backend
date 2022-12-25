from django.db import models

#Base Product Model
class Product(models.Model):
    name = models.CharField(max_length=500)
    description = models.CharField(max_length=2000)
    price = models.CharField(max_length=100)
    stock = models.IntegerField(default=20)
    image = models.CharField(max_length=1000)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name
    