from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('sign-up',views.sign_up,name='sign-up'),
    path('sign-in',views.sign_in,name='sign-in'),
    path('forgot-password',views.forgot_password,name='forgot-password'),
    path('profile',views.profile,name='profile'),
]