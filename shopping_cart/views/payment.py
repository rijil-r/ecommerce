from rest_framework import permissions, viewsets

from shopping_cart.models import Payment
from shopping_cart.serializers.payment import PaymentSerializer


class PaymentViewSet(viewsets.ModelViewSet):
    """
    The PaymentViewSet class is a viewset for the Payment model for authenticated users.

    Fields:
    serializer_class: The serializer class used for the Payment model. It's set to PaymentSerializer.
    permission_classes: The permission classes for the viewset. It's set to IsAuthenticated, which means only authenticated users can access this viewset.

    Methods:
    get_queryset: Returns the queryset that should be used for list views, and that should be used as the base for lookups of individual instances.
    """
    serializer_class = PaymentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """
        Returns the queryset that should be used for list views, and that should be used as the base for lookups of individual instances.

        In this case, it returns all Payment objects that belong to the currently authenticated user.
        """
        user = self.request.user
        return Payment.objects.filter(order__customer=user)


class PaymentAdminViewSet(viewsets.ModelViewSet):
    """
    The PaymentAdminViewSet class is a viewset for the Payment model for admin users.

    Fields:
    queryset: The initial queryset that should be used for list views, and that should be used as the base for lookups of individual instances. It's set to all Payment objects.
    serializer_class: The serializer class used for the Payment model. It's set to PaymentSerializer.
    permission_classes: The permission classes for the viewset. It's set to IsAdminUser, which means only admin users can access this viewset.

    Methods:
    get_queryset: Returns the queryset that should be used for list views, and that should be used as the base for lookups of individual instances.
    """
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [permissions.IsAdminUser]

    def get_queryset(self):
        """
        Returns the queryset that should be used for list views, and that should be used as the base for lookups of individual instances.

        In this case, it returns all Payment objects.
        """
        return Payment.objects.all()