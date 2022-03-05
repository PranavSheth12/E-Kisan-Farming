from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=50,default="")
    email = models.EmailField(max_length=254,default="")
    phone = models.IntegerField(default=0)
    message = models.TextField(max_length=500,default="")

    def __str__(self):
        return self.email