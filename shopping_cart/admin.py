from django.contrib import admin

from shopping_cart.models import Order, Product, Payment
from shopping_cart.models.order import OrderProduct
from shopping_cart.models.product import Category

# Register your models here.
admin.site.register(Order)
admin.site.register(Product)
admin.site.register(Payment)
admin.site.register(Category)
admin.site.register(OrderProduct)
