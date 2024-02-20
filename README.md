
# Integration of Stripe Payment in a Django Application

The integration involves setting up a Stripe account, obtaining API keys from Stripe, configuring these credentials in your Django settings file, and implementing various views within your Django application to handle user interactions with the payment system.





## Installation

Clone the repository from GitHub:

```
  https://github.com/geetamamde/Stripe_Payment_Gateway.git

  cd Stripe_Payment_Gateway
```

Run the command

```
   pip install stripe
```
after setting up the STRIPE_PUBLISHABLE_KEY and STRIPE_SECRET_KEY

Run the database migrations:
```
python manage.py makemigration

python manage.py migrate 

```
Create a superuser

```
python manage.py createsuperuser
```

Run the server
```
python manage.py runserver
```
## Screenshots

Home page

![home](https://github.com/geetamamde/Stripe_Payment_Gateway/assets/105689568/3da0b786-e927-4c60-8472-034531e09c5a)

CheckOut page

![checkout](https://github.com/geetamamde/Stripe_Payment_Gateway/assets/105689568/5e799ee1-f543-42dc-846d-983c5e74ab41)


Stripe dashboard 

![payment dashboard](https://github.com/geetamamde/Stripe_Payment_Gateway/assets/105689568/7c9969a1-2595-4eb3-9d37-13661230ab47)



