from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('profile-customer',views.profile_customer,name='profile-customer'),
]