# Django management command to add data to the database

from django.core.management.base import BaseCommand

from shopping_cart.models import Category, Product, Payment
from shopping_cart.models.order import Order, OrderProduct
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Add data to the database'

    def handle(self, *args, **kwargs):
        # Make bulk data for all models
        categories = ['Electronics', 'Clothing', 'Books', 'Furniture']
        products = [
            {'name': 'Laptop', 'price': 500, 'description': 'Dell Laptop', 'category': 'Electronics'},
            {'name': 'T-shirt', 'price': 10, 'description': 'Polo T-shirt', 'category': 'Clothing'},
            {'name': 'Python Crash Course', 'price': 30, 'description': 'Python Crash Course', 'category': 'Books'},
            {'name': 'Table', 'price': 100, 'description': 'Wooden Table', 'category': 'Furniture'},
        ]
        users = [
            {'username': 'user1', 'password': 'user1', 'email': 'example1@example.com'},
            {'username': 'user', 'password': 'user', 'email': 'example@example.com'    },
        ]
        orders = [
            {'customer': 'admin', 'products': [
                {'product': 'Laptop', 'quantity': 2},
                {'product': 'T-shirt', 'quantity': 3},
            ]},
            {'customer': 'user', 'products': [
                {'product': 'Python Crash Course', 'quantity': 1},
                {'product': 'Table', 'quantity': 1},
            ]},
        ]

        # Create categories
        for category in categories:
            Category.objects.create(name=category)

        # Create superuser
        User.objects.create_superuser('admin', 'admin@example.com', 'password')

        # Create products
        for product in products:
            category = Category.objects.get(name=product['category'])
            Product.objects.create(name=product['name'], price=product['price'], description=product['description'], category=category)

        # Create users
        for user in users:
            User.objects.create_user(username=user['username'], password=user['password'], email=user['email'])

        # Create orders
        for order in orders:
            customer = User.objects.get(username=order['customer'])
            new_order = Order.objects.create(customer=customer)
            for product in order['products']:
                item = Product.objects.get(name=product['product'])
                order_product = OrderProduct.objects.create(product=item, quantity=product['quantity'])
                order_product.order.add(new_order)
            Payment.objects.create(order=new_order, status='pending', method='card')
        self.stdout.write(self.style.SUCCESS('Data added successfully'))
