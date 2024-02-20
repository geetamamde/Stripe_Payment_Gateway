from django.shortcuts import render,redirect
import stripe
from django.conf import settings
from .models import Order,Product,Payment
from django.shortcuts import render, redirect
from django.contrib.auth import login,logout, authenticate
from django.views import View
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect,HttpResponseBadRequest,HttpResponse
from django.contrib import messages
from .models import *
import stripe
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.

# View to render the home page with all products
@login_required(login_url='signin/')
def home(request):
    products = Product.objects.all()
    return render(request,"home.html",{'products':products})



# View to display details of a product
def details(request,id):
    product = Product.objects.get(id=id)
    return render(request,"view.html",{'product':product})

# View to create a checkout session for purchasing a product
def create_checkout_session(request,id):
    product = Product.objects.get(id=id)
    stripe.api_key = settings.STRIPE_SECRET_KEY
    order = Order.objects.create(user = request.user, product = product)
    order.save()
    
    try:
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],

            line_items=[
                {
                  'price_data': {
                    'currency': 'usd',
                    'product_data': {
                    'name': product.name,
                    },
                     'unit_amount':product.price*100,
                    
                },
                'quantity': 1,
                }
            ],
            mode='payment',
        
            success_url= 'http://127.0.0.1:8000/payment-successful?session_id={CHECKOUT_SESSION_ID}',
            cancel_url= 'http://127.0.0.1:8000/payment-cancelled',
)
    except:
        pass

    return redirect(checkout_session.url, code=303)

# View for handling successful payment
def payment_successful(request): 
    session = stripe.checkout.Session.retrieve(request.GET['session_id'])

    payment = Payment.objects.create(user=request.user,stripe_payment_id=session)
    payment.save()
    return render(request, 'success.html')

# View for handling cancelled payment
def payment_cancelled(request):
	return render(request, 'cancle.html')

# View for user registration
class SignUpView(View):
    template = 'app/signup.html'
    def get(self, request, *args, **kwargs):
        return render(request, self.template)
    
    def post(self, request, *args, **kwargs):
        form = request.POST
        if form['password'] == form['confirmpassword']:
            try:
                new_user = User.objects.create_user(username=form['name'],password=form['password'])
                new_user.email = form['email']
                new_user.save()

                return redirect('home')
            except:
                messages.add_message(request, messages.INFO, "username already exist!")
        else:
            messages.add_message(request, messages.ERROR, "Password didn't match!")

        return render(request, self.template)

# View for user login
class SignInView(View):
    template = 'app/signin.html'
    def get(self, request, *args, **kwargs):
        return render(request, self.template)

    def post(self, request, *args, **kwargs):
        form = request.POST
        try:
            user = User.objects.get(username = form['name'])
            try:
                user = authenticate(username=form['name'],password=form['password'])
                login(request, user)
                return redirect('home')
            
            except:
                messages.add_message(request, messages.ERROR, "username or password is incorect")
        except:
            messages.add_message(request, messages.ERROR, "username doesn't exist!")
        return render(request, self.template)
