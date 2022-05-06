import email
from pickle import TRUE
from django.db import models
from django.contrib.auth.models import  User
from django.db.models.deletion import CASCADE

# Create your models here.

class CustomUser(models.Model):
    
    username = models.CharField(max_length=50,default="",unique=True)

    name = models.CharField(max_length=50,default="")
    profile_pic  = models.FileField(upload_to='profile_pic',help_text='Image should be in jpeg/jpg/png form and image size should be 250*250')
    date_of_birth = models.DateField()
    category = models.CharField(max_length=50,default="")
    email = models.EmailField(max_length=254,default="")
    phone = models.IntegerField(default=0)


    def __str__(self):
        return self.username
    