import json
from django.core import serializers
import requests
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
            user = request.user
            user = CustomUser.objects.get(username = user.username)
            
            if user.category == 'farmer':
                return redirect('profile')
            else:
                return redirect('profile-customer')
        else:
            messages.error(request, 'Wrong username or password')
            return render(request,'signin.html',)
    return render(request,'signin.html')

def sign_up(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        x = User.objects.filter(username=username)

        password = request.POST.get('password')
        repassword = request.POST.get('repassword')

        if password != repassword:
            messages.success(request,"password does not match")
            return render(request,'signup.html')



        if not x:
        
            name = request.POST.get('name')
            profile_pic = request.FILES['profile_pic']
            email = request.POST.get('email')
            date_of_birth = request.POST.get('date_of_birth')
            phone = request.POST.get('phone')
            category = request.POST.get('category')

            # password = request.POST.get('password')
            print(profile_pic)
            user = User.objects.create_user(username=username, email=email,password=f'{password}')
            user.save()
            customUser = CustomUser(username = username,name = name, email = email,date_of_birth = date_of_birth,profile_pic = profile_pic, phone=phone,category=category )
            customUser.save()
            
            messages.success(request,"You have signed up successfully")
            return redirect('sign-in')
        else:
            messages.success(request,"Username is already taken")
        return render(request,'signup.html')
    return render(request,'signup.html')

def sign_out(request):
    logout(request)
    messages.success(request,"Logged out successfully")
    return redirect('home')
    
def forgot_password(request):

    if request.method == "POST":

        condt = request.POST.get('condt')
        print(condt)

        if condt == "first":

            username = request.POST.get('username')

            user = CustomUser.objects.get(username = username)
            request.session['username'] = username

            if user is not None:
                phone = user.phone
                a = requests.get('https://2factor.in/API/V1/5c7b9774-8f27-11eb-a9bc-0200cd936042/SMS/' + str(phone) + '/AUTOGEN')
                b = json.loads(a.text)
                print(a,b)
                id = b['Details']
                request.session['id'] = id

                condt = "second"
                return render(request, 'forgot-password.html',{'condt':condt})
            else:
                messages.error(request, 'username is invalid')
                return render(request, 'forgot-password.html',{'condt':condt})


        elif condt == "second":

            username = request.session.get('username')
            id = request.session.get('id')

            otp = request.POST.get('OTP')
            password = request.POST.get('password')
            c = requests.get('https://2factor.in/API/V1/5c7b9774-8f27-11eb-a9bc-0200cd936042/SMS/VERIFY/'+ id + '/' + str(otp))
            print(c)
            d = json.loads(c.text)
            print(d)
            print(type(d))
            if d['Details'] == 'OTP Matched':
                print('yes')
                user1 = User.objects.get(username=username)
                user1.set_password(f'{password}')
                user1.save()
                messages.success(request, 'Your password has been successfully changed')
                return redirect('home')
            else:
                messages.error(request, 'OTP is invalid')
                return render(request, 'forgot-password.html',{'condt':condt})

    condt = "first"
    return render(request,'forgot-password.html',{'condt':condt})

