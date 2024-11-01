from django.contrib import admin

# Register your models here.
from .models import Product, Customer, Order, OrderItem, Cart, CartItem

admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Cart)
admin.site.register(CartItem)