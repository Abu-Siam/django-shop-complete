from django.contrib import admin
from django.contrib.auth.models import User

from .models import Product, Customer, Cart, OrderPlaced
# Register your models here.


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'selling_price', 'discounted_price', 'description', 'brand', 'category', 'product_image']

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['user', 'name', 'state', 'locality', 'city', 'zipcode']

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'quantity']



@admin.register(OrderPlaced)
class OrderPlacedAdmin(admin.ModelAdmin):
    list_display = ['user', 'customer', 'product', 'quantity', 'ordered_date', 'status']


# class OrderInline(admin.TabularInline):
#     model = OrderPlaced
#     extra = 5
#
# #
# class CustomAdmin(admin.ModelAdmin):
#     inlines = [OrderInline]
#     # list_display = ["use", "selling_price", "discounted_price", "description",]
#     list_display = [ 'name', 'state', 'locality', 'city', 'zipcode']
# #
# #
# admin.site.register(Customer,CustomAdmin)
# admin.site.register(Customer)