# import router
from django.urls import path
from rest_framework.routers import DefaultRouter

from shopping_cart.views.order import OrderModelViewSet, OrderAdminModelViewSet
from shopping_cart.views.payment import PaymentViewSet, PaymentAdminViewSet
from shopping_cart.views.product import ProductViewSet
from shopping_cart.views.home import HomeView
from shopping_cart.views.user import UserViewSet

# Create a default router
router = DefaultRouter()

# Register the viewsets with the router
router.register('orders', OrderModelViewSet, basename='order')
router.register('admin/orders', OrderAdminModelViewSet, basename='admin-order')
router.register('payments', PaymentViewSet, basename='payment')
router.register('admin/payments', PaymentAdminViewSet, basename='admin-payment')
router.register('products', ProductViewSet, basename='product')
router.register('user', UserViewSet, basename='user')

urlpatterns = [
    # URL patterns for the Django template view
    path('', HomeView.as_view(), name='home'),
]