from django.db import models
import uuid
from django.contrib.auth.models import AbstractUser

#USER MODEL
class MyUser(AbstractUser):
    uid = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True)
    USERNAME_FIELD = 'email' #using the email as the identifier instead of username
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=60)
    date_of_birth = models.DateField()
    username = None 
    phone = models.CharField( max_length=100, null=True)
    email_verified = models.BooleanField(default=False)
    REQUIRED_FIELDS = ['first_name', 'last_name'] # making some fields compulsory

    def __str__(self):
        return self.email
    
#OTP MODEL
class OTP(models.Model):
    otp_request_id = models.UUIDField(default=uuid.uuid4, unique=True)


    def __str__(self):
        return self.requested_by
    