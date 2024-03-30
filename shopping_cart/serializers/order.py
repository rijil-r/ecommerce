from rest_framework import serializers

from shopping_cart.models import Order
from shopping_cart.models.order import OrderProduct


class OrderProductSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product.name', read_only=True)

    class Meta:
        model = OrderProduct
        fields = ['product', 'quantity', 'product_name', 'total']


class OrderSerializer(serializers.ModelSerializer):
    items = OrderProductSerializer(many=True, source='products')

    class Meta:
        model = Order
        fields = ['id', 'customer', 'items', 'amount', 'status']
