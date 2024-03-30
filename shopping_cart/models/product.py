from django.db import models

from shopping_cart.models.base import ActivityLogger


class Category(ActivityLogger):
    """
    The Category model represents a category of products.

    Each Category has a unique name.

    Fields:
    name: The name of the category. It's a unique char field.

    Inherits from:
    ActivityLogger: An abstract model that adds created and updated fields to the model.
    """
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        """
        Returns a string representation of the Category.

        The string is the name of the category.
        """
        return self.name


class Product(ActivityLogger):
    """
    The Product model represents a product.

    Each Product has a name, price, description, image, and a foreign key relationship with the Category model,
    which represents the category the product belongs to.

    Fields:
    name: The name of the product. It's a char field.
    price: The price of the product. It's a float field with a default value of 0.
    description: The description of the product. It's a text field.
    image: The image of the product. It's an image field that uploads to 'products/'.
    category: The category the product belongs to. It's a foreign key relating to the Category model.

    Inherits from:
    ActivityLogger: An abstract model that adds created and updated fields to the model.
    """
    name = models.CharField(max_length=255)
    price = models.FloatField(default=0)
    description = models.TextField()
    image = models.ImageField(upload_to='products/', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        """
        Returns a string representation of the Product.

        The string is the name of the product.
        """
        return self.name
