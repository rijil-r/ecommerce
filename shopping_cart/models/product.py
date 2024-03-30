from django.db import models

from shopping_cart.models.base import ActivityLogger


class Category(ActivityLogger):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Product(ActivityLogger):
    name = models.CharField(max_length=255)
    price = models.FloatField(default=0)
    description = models.TextField()
    image = models.ImageField(upload_to='products/', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
