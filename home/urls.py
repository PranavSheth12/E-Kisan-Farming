from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('contact-us',views.contact_us,name='contact-us'),
    path('products',views.products,name='products'),
    path('cart/',views.cart,name='cart'),
    path('aboutus',views.aboutus,name='aboutus'),
    path('contractfarming',views.contractfarming,name='contractfarming'),
]