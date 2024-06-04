from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    age = models.IntegerField()
    address = models.TextField(max_length=200)
    mobile_no = models.CharField(max_length=10)
    date = models.DateTimeField()

# python manage.py makemigrations 
# python manage.py migrate 
