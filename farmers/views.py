from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User


# Create your views here.

def profile(request):

    user  = request.user
    

    return render(request,'profile.html')



   