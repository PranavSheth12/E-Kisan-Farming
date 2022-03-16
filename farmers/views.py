from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from accounts.models import CustomUser

# Create your views here.

def profile(request):

    if request.user.is_authenticated:
        user  = request.user
        user = CustomUser.objects.get(username = user.username)

        return render(request,'profile.html',{'customuser' : user})
    else:
        return redirect('sign-in')



   