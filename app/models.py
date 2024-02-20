from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.utils import timezone
# Create your models here.
"""
    Represents a product available for purchase.

    Attributes:
        name (str): The name of the product.
        desc (str): Description of the product.
        price (int): The price of the product.
        img (str): Path to the product image.
    """
class Product(models.Model):
    name = models.CharField(max_length=45)
    desc = models.TextField()
    price=models.IntegerField()
    img = models.ImageField(upload_to='img',default='no')

    def __str__(self):
        return self.name


   """
    Represents an order placed by a user.

    Attributes:
        user (User): The user who placed the order.
        product (Product): The product ordered.
        date_time (datetime): The date and time when the order was placed.
    """
class Order(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    date_time = models.DateTimeField(default=timezone.now)


"""
    Represents a payment made by a user.

    Attributes:
        user (User): The user who made the payment.
        stripe_payment_id (str): The Stripe payment ID associated with the payment.
    """
class Payment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    stripe_payment_id = models.CharField(max_length=200,blank=True, null=True)

   