from django.contrib import admin
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