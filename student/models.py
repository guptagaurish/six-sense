from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class stud(models.Model):
    
    name = models.CharField(max_length=30)
    contact = PhoneNumberField()
    email = models.EmailField(max_length=30)
    dob = models.CharField(max_length=30) #
    
# Create your models here.
