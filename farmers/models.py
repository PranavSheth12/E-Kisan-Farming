from django.db import models

# Create your models here.


class myproduct(models.Model):

    name = models.CharField(max_length=50,default="")
    sown = models.DateField()
    reap = models.DateField()
    land_area = models.BigIntegerField(default=0)
    area = models.CharField(max_length=50, default="")
