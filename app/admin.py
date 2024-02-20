from django.contrib import admin
from .models import Payment,Product,Order
# Register your models here.

admin.site.register(Product)
admin.site.register(Payment)
admin.site.register(Order)