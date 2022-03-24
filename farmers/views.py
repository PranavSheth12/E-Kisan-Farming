from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from accounts.models import CustomUser
from farmers.models import myproduct

# Create your views here.

def profile(request):

    if request.user.is_authenticated:
        user  = request.user
        user = CustomUser.objects.get(username = user.username)

        products = myproduct.objects.filter(user = user)
        print(products)

        return render(request,'profile.html',{'customuser' : user, 'products' : products})
    else:
        return redirect('sign-in')



   