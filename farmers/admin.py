from django.contrib import admin
from .models import myproduct,Cart,OrderPlaced

# Register your models here.
admin.site.register(myproduct)
admin.site.register(Cart)
admin.site.register(OrderPlaced)
