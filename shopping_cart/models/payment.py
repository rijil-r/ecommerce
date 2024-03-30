from django.db import models

from shopping_cart.models.base import ActivityLogger
from shopping_cart.models.order import Order


class PaymentStatus(models.TextChoices):
    PENDING = 'pending'
    COMPLETED = 'completed'
    CANCELLED = 'cancelled'
    REFUND = 'refund'


class PaymentMode(models.TextChoices):
    CASH = 'cash'
    CARD = 'card'
    BANK = 'bank'


class Payment(ActivityLogger):
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, choices=PaymentStatus.choices, default=PaymentStatus.PENDING)
    method = models.CharField(max_length=50, choices=PaymentMode.choices, default=PaymentMode.CARD)
