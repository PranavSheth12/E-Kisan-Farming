from django.db import models
from django.contrib.auth.models import  User
from accounts.models import CustomUser
# Create your models here.
class myproduct(models.Model):

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    image = models.FileField(upload_to='products',help_text='Image should be in jpeg/jpg/png form and image size should be 250*250')
    name = models.CharField(max_length=50,default="")
    sown = models.DateField()
    reap = models.DateField()
    land_area = models.BigIntegerField(default=0)
    address = models.CharField(max_length=50, default="")

    
    def __str__(self):
        return self.name
