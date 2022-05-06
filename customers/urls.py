from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('profile-customer',views.profile_customer,name='profile-customer'),
    path('add-to-cart/', views.add_to_cart, name='add-to-cart'),
    path('cart/', views.show_cart, name='showcart'),
    path('pluscart/', views.plus_cart),
    path('minuscart/', views.minus_cart),
    path('removecart/', views.remove_cart),
    path('checkout/', views.checkout,name='checkout'),
    path('order-placed/', views.order_placed,name='order-placed'),
]