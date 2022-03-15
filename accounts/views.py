from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from .models import CustomUser
# Create your views here.
def sign_in(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            # messages.success(request, 'Logged in successfully')
            return redirect('profile')
        else:
            #messages.error(request, 'Wrong username or password')
            return render(request,'signin.html',)
    return render(request,'signin.html')

def sign_up(request):
    if request.method == 'POST':

        username = request.POST.get('username')
        name = request.POST.get('name')
        profile_pic = request.FILES['profile_pic']
        email = request.POST.get('email')
        date_of_birth = request.POST.get('date_of_birth')
        phone = request.POST.get('phone')
        category = request.POST.get('category')

        password = request.POST.get('password')
        print(profile_pic)
        user = User.objects.create_user(username=username, email=email,password=f'{password}')
        user.save()
        customUser = CustomUser(username = username,name = name, email = email,date_of_birth = date_of_birth,profile_pic = profile_pic, phone=phone,category=category )
        customUser.save()
        
        # messages.success(request,"You have signed up successfully")
        return redirect('home')
    return render(request,'signup.html')

def sign_out(request):
    logout(request)
    messages.success(request,"Logged out successfully")
    return redirect('home')
    
def forgot_password(request):
    return render(request,'forgot-password.html')

