from django.db import models
from django.contrib.auth.models import User
from accounts.models import CustomUser
# Create your models here.

CATEGORY_CHOICES = (
    ('M', 'Mobile'),
    ('L', 'Laptop'),
    ('TW', 'Top Wear'),
    ('BW', 'Bottom Wear'),
)

class myproduct(models.Model):

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    # image = models.FileField(upload_to='products', help_text='Image should be in jpeg/jpg/png form and image size should be 250*250')
    sown = models.DateField()
    reap = models.DateField()
    land_area = models.BigIntegerField(default=0)
    address = models.CharField(max_length=50, default="")
    title = models.CharField(max_length=100)
    selling_price = models.FloatField()
    discounted_price = models.FloatField()
    description = models.TextField()
    product_image = models.ImageField(upload_to='products', help_text='Image should be in jpeg/jpg/png form and image size should be 250*250')

    def __str__(self):
        return str(self.id)


class Cart(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    product = models.ForeignKey(myproduct, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)

        # Below Property will be used by checkout.html page to show total cost in order summary
    @property
    def total_cost(self):
        return self.quantity * self.product.discounted_price

STATUS_CHOICES = (
    ('Accepted', 'Accepted'),
    ('Packed', 'Packed'),
    ('On The Way', 'On The Way'),
    ('Delivered', 'Delivered'),
    ('Cancel', 'Cancel')
)
class OrderPlaced(models.Model):
    customer = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    product = models.ForeignKey(myproduct, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    ordered_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
    max_length=50, choices=STATUS_CHOICES, default='Pending')

    # Below Property will be used by orders.html page to show total cost
    @property
    def total_cost(self):
        return self.quantity * self.product.discounted_price

    def __str__(self):
        return str(self.id)