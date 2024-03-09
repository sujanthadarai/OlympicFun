from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class signup(models.Model):
    name=models.CharField(max_length=50)
    country=models.CharField(max_length=100)
    phone=PhoneNumberField()
    username=models.CharField(max_length=200)
    email=models.EmailField(unique=True)
    interest_sports=models.CharField(max_length=200)
    password=models.CharField(max_length=200)
    confirm_password=models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name
    
class signin(models.Model):
    username=models.CharField(max_length=200)
    password=models.CharField(max_length=200)
    confirm_password=models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.username




