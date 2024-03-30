from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.viewsets import ModelViewSet

from shopping_cart.models import Order
from shopping_cart.serializers.order import OrderSerializer


class OrderModelViewSet(ModelViewSet):
    """
    The OrderModelViewSet class is a viewset for the Order model.

    Fields:
    serializer_class: The serializer class used for the Order model. It's set to OrderSerializer.
    permission_classes: The permission classes for the viewset. It's set to IsAuthenticated, which means only authenticated users can access this viewset.

    Methods:
    get_queryset: Returns the queryset that should be used for list views, and that should be used as the base for lookups of individual instances.
    """
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        Returns the queryset that should be used for list views, and that should be used as the base for lookups of individual instances.

        In this case, it returns all Order objects that belong to the currently authenticated user.
        """
        user = self.request.user
        return Order.objects.filter(customer=user)


class OrderAdminModelViewSet(ModelViewSet):
    """
    The OrderAdminModelViewSet class is a viewset for the Order model for admin users.

    Fields:
    queryset: The initial queryset that should be used for list views, and that should be used as the base for lookups of individual instances. It's set to all Order objects.
    serializer_class: The serializer class used for the Order model. It's set to OrderSerializer.
    permission_classes: The permission classes for the viewset. It's set to IsAdminUser, which means only admin users can access this viewset.

    Methods:
    get_queryset: Returns the queryset that should be used for list views, and that should be used as the base for lookups of individual instances.
    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        """
        Returns the queryset that should be used for list views, and that should be used as the base for lookups of individual instances.

        In this case, it returns all Order objects.
        """
        return Order.objects.all()