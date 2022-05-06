from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from accounts.models import CustomUser
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.conf import settings
from django.core.mail import send_mail


from farmers.models import myproduct, Cart, OrderPlaced

# Create your views here.


def profile_customer(request):

    if request.user.is_authenticated:
        user  = request.user
        user = CustomUser.objects.get(username = user.username)

        orders = OrderPlaced.objects.filter(customer = user)
        print(orders)

        return render(request, 'profile-customer.html',{'customuser' : user, 'orders' : orders})
    else:
        return redirect('sign-in')


@login_required(login_url='/accounts/sign-in')
def add_to_cart(request):
    user = request.user
    user = CustomUser.objects.get(username=user.username)
    item_already_in_cart1 = False
    product = request.GET.get('prod_id')
    print(product)
    item_already_in_cart1 = Cart.objects.filter(
        Q(product=product) & Q(user=user)).exists()
    if item_already_in_cart1 == False:
        product_title = myproduct.objects.get(id=product)
        Cart(user=user, product=product_title).save()
        messages.success(request, 'Product Added to Cart Successfully !!')
        return redirect('showcart')
    else:
        return redirect('showcart')
  # Below Code is used to return to same page
  # return redirect(request.META['HTTP_REFERER'])


@login_required(login_url='/accounts/sign-in')
def show_cart(request):
    totalitem = 0
    if request.user.is_authenticated:
        user = request.user
        user = CustomUser.objects.get(username=user.username)

        cart = Cart.objects.filter(user=user)
        totalitem = len(Cart.objects.filter(user=user))

        amount = 0.0
        shipping_amount = 0.0
        totalamount = 0.0
        cart_product = [p for p in Cart.objects.all() if p.user == user]
        print(cart_product)
        if cart_product:
            for p in cart_product:
                tempamount = (p.quantity * p.product.discounted_price)
                amount += tempamount
            totalamount = amount+shipping_amount
            return render(request, 'cart.html', {'carts': cart, 'amount': amount, 'totalamount': totalamount, 'totalitem': totalitem})
        else:
            return render(request, 'cart.html', {'totalitem': totalitem})
    else:
        return render(request, 'cart.html', {'totalitem': totalitem})


def plus_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        user = request.user
        user = CustomUser.objects.get(username=user.username)

        c = Cart.objects.get(Q(product=prod_id) & Q(user=user))
        c.quantity += 1
        c.save()
        amount = 0.0
        shipping_amount = 0.0
        cart_product = [p for p in Cart.objects.all() if p.user == user]
        for p in cart_product:
            tempamount = (p.quantity * p.product.discounted_price)
            # print("Quantity", p.quantity)
            # print("Selling Price", p.product.discounted_price)
            # print("Before", amount)
            amount += tempamount
            # print("After", amount)
        # print("Total", amount)
        data = {
            'quantity': c.quantity,
            'amount': amount,
            'totalamount': amount+shipping_amount
        }
        return JsonResponse(data)
    else:
        return HttpResponse("")


def minus_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        user = request.user
        user = CustomUser.objects.get(username=user.username)
        c = Cart.objects.get(Q(product=prod_id) & Q(user=user))
        c.quantity -= 1
        c.save()
        amount = 0.0
        shipping_amount = 0.0
        cart_product = [p for p in Cart.objects.all() if p.user == user]
        for p in cart_product:
            tempamount = (p.quantity * p.product.discounted_price)
            # print("Quantity", p.quantity)
            # print("Selling Price", p.product.discounted_price)
            # print("Before", amount)
            amount += tempamount
            # print("After", amount)
        # print("Total", amount)
        data = {
            'quantity': c.quantity,
            'amount': amount,
            'totalamount': amount+shipping_amount
        }
        return JsonResponse(data)
    else:
        return HttpResponse("")


def remove_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        user = request.user
        user = CustomUser.objects.get(username=user.username)
        c = Cart.objects.get(Q(product=prod_id) & Q(user=user))
        c.delete()
        amount = 0.0
        shipping_amount = 0.0
        cart_product = [p for p in Cart.objects.all() if p.user == user]
        for p in cart_product:
            tempamount = (p.quantity * p.product.discounted_price)
            # print("Quantity", p.quantity)
            # print("Selling Price", p.product.discounted_price)
            # print("Before", amount)
            amount += tempamount
            # print("After", amount)
        # print("Total", amount)
        data = {
            'amount': amount,
            'totalamount': amount+shipping_amount
        }
		
        return JsonResponse(data)
    else:
        return HttpResponse("")


def checkout(request):


	user = request.user
	user = CustomUser.objects.get(username=user.username)

	id = user.id
	request.session['custid'] = id
	cart = Cart.objects.filter(user=user)
	print(cart)
	products = ''

	for c in cart:
		products = products+f'{c.product.title}-{c.quantity}\n'

	# print(products)
	send_mail(
		'Order confirmation',
		f'Hey {user.name}, \nyour order is: \n{products}',
		f'{settings.EMAIL_HOST_USER}',
		[user.email, ],
		fail_silently=False,
	)
	return redirect('order-placed')

def order_placed(request):

	custid = request.session.get('custid')
	print("Customer ID", custid)

	user = request.user
	customer = CustomUser.objects.get(username=user.username)

	cartid = Cart.objects.filter(user = customer)
	# customer = CustomUser.objects.get(id=custid)
	print(customer)
	for cid in cartid:
		OrderPlaced(customer=customer, product=cid.product, quantity=cid.quantity).save()
		print("Order Saved")
		cid.delete()
		print("Cart Item Deleted")

	messages.success(request, 'Your order has been successfully submitted. Check your email for confirmation.')
	return redirect("home")