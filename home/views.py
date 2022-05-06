from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Contact
from farmers.models import myproduct
# Create your views here.
def home(request):
    return render(request,'index.html')

def contact_us(request):
    
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        contact = Contact(name=name,email=email,phone=phone,message=message)
        contact.save()

        messages.success(request, 'Your message has been sent.')
        return redirect('home')
    return render(request,'contact-us.html')

def products(request):

    products = myproduct.objects.all()
    
    return render(request,'products.html',{'products':products})


def cart(request):
    return render(request,'cart.html')

def aboutus(request):
    return render(request,'aboutus.html')

def contractfarming(request):
    return render(request,'contractfarming.html')