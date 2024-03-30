from rest_framework import viewsets, permissions

from shopping_cart.models import Product
from shopping_cart.serializers.product import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    """
    The ProductViewSet class is a viewset for the Product model.

    Fields:
    queryset: The initial queryset that should be used for list views, and that should be used as the base for lookups of individual instances. It's set to all Product objects.
    serializer_class: The serializer class used for the Product model. It's set to ProductSerializer.
    permission_classes: The permission classes for the viewset. It's set to IsAuthenticatedOrReadOnly or IsAdminUser, which means only authenticated users or admin users can access this viewset.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly or permissions.IsAdminUser]
