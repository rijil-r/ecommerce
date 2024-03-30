from rest_framework import serializers

from shopping_cart.models import Payment


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['id', 'order', 'status', 'method', 'created']
