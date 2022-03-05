import email
from pickle import TRUE
from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class CustomUser(models.Model):
    
    username = models.CharField(max_length=50,default="",unique=TRUE)
    category = models.CharField(max_length=50,default="")
    email = models.EmailField(max_length=254,default="")
    phone = models.IntegerField(default=0)
    password = models.CharField(max_length=50,default="")

    def __str__(self):
        return self.username
    