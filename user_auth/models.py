from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class MyUser(AbstractUser):
    email = models.EmailField(unique=True)
    USERNAME_FIELD = 'email' #using the email as the identifier instead of username
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=60)
    date_of_birth = models.DateField()
    REQUIRED_FIELDS = ['first_name', 'last_name'] # making all fields compulsory

    def __str__(self):
        return self.email
    