from django.contrib.auth.models import User
from django.db import models

from shopping_cart.models.base import ActivityLogger
from shopping_cart.models.product import Product


class Order(ActivityLogger):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.customer}-{self.amount}'

    @property
    def amount(self):
        return sum([product.total for product in self.products.all()])

    @property
    def status(self):
        if hasattr(self, 'payment'):
            return self.payment.status
        return 'Pending'


class OrderProduct(ActivityLogger):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    order = models.ManyToManyField(Order, related_name='products')


    class Meta:
        unique_together = ['product', 'quantity']

    def __str__(self):
        return f'{self.product.name} x {self.quantity}'



    @property
    def total(self):
        return self.product.price * self.quantity
