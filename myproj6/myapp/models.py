from django.db import models

# Create your models here.

class RegisterModel(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    age = models.IntegerField()
    address = models.CharField(max_length=100)
    mobile = models.CharField(max_length=100)
    data = models.DateField()