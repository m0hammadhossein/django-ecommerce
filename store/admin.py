from django.contrib import admin
from .models import *

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('user','name','email')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','price','digital')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer','date_ordered')

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('product','order','quantity')

@admin.register(ShippingAddress)
class ShippingAddressAdmin(admin.ModelAdmin):
    list_display = ('customer','order','address')