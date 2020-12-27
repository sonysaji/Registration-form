from django.db import models


# Create your models here.
class registration(models.Model):
    first_name=models.CharField(max_length=200)
    last_name=models.CharField(max_length=200)
    mobile=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    gender=models.CharField(max_length=200)
    password=models.CharField(max_length=200)
    

