from rest_framework import viewsets, permissions

from shopping_cart.models import Product
from shopping_cart.serializers.product import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly or permissions.IsAdminUser]
