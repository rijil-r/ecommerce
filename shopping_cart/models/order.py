from django.contrib.auth.models import User
from django.db import models

from shopping_cart.models.base import ActivityLogger
from shopping_cart.models.product import Product


class Order(ActivityLogger):
    """
    The Order model represents an order placed by a customer.

    Each Order has a foreign key relationship with the User model,
    which represents the customer who placed the order.

    Fields:
    customer: The customer who placed the order. It's a foreign key relating to the User model.

    Model Properties:
    amount: Calculates and returns the total amount for the order.
    status: Returns the status of the payment for the order.
    """

    customer = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """
        Returns a string representation of the Order.

        The string includes the name of the customer and the total amount of the order.
        """
        return f'{self.customer}-{self.amount}'

    @property
    def amount(self):
        """
        Calculates and returns the total amount for the Order.

        The total amount is calculated as the sum of the total price of all products in the order.
        """
        return sum([product.total for product in self.products.all()])

    @property
    def status(self):
        """
        Returns the status of the payment for the Order.

        If the order has a related payment, it returns the status of the payment.
        Otherwise, it returns 'Pending'.
        """
        if hasattr(self, 'payment'):
            return self.payment.status
        return 'Pending'


class OrderProduct(ActivityLogger):
    """
    The OrderProduct model represents a product that is part of an order.

    Each OrderProduct has a foreign key relationship with the Product model,
    which represents the product being ordered, and a many-to-many relationship
    with the Order model, which represents the order(s) the product is part of.

    Fields:
    product: The product being ordered. It's a foreign key relating to the Product model.
    quantity: The quantity of the product being ordered. It defaults to 1.
    order: The order(s) this product is part of. It's a many-to-many field relating to the Order model.

    Model Properties:
    total: Calculates and returns the total price for the OrderProduct.
    """

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    order = models.ManyToManyField(Order, related_name='products')

    class Meta:
        unique_together = ['product', 'quantity']

    def __str__(self):
        """
        Returns a string representation of the OrderProduct.

        The string includes the name of the product and its quantity.
        """
        return f'{self.product.name} x {self.quantity}'

    @property
    def total(self):
        """
        Calculates and returns the total price for this OrderProduct.

        The total price is calculated as the product's price times its quantity.
        """
        return self.product.price * self.quantity