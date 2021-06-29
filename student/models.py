from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class stud(models.Model):
    
    name = models.CharField(max_length=30)
    auth_token = models.CharField(max_length=100,default=" ")
    is_verified = models.BooleanField(default=False)
    contact = PhoneNumberField()
    email = models.EmailField(max_length=30)
    dob = models.CharField(max_length=30) #
    
# Create your models here.
