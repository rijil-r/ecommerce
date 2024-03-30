from django.db import models

from shopping_cart.models.base import ActivityLogger
from shopping_cart.models.order import Order


class PaymentStatus(models.TextChoices):
    """
    The PaymentStatus class represents the different statuses a payment can have.

    It's a subclass of Django's TextChoices, which allows for easier creation of choices for a CharField.

    Choices:
    PENDING: The payment is pending.
    COMPLETED: The payment has been completed.
    CANCELLED: The payment has been cancelled.
    REFUND: The payment has been refunded.
    """
    PENDING = 'pending'
    COMPLETED = 'completed'
    CANCELLED = 'cancelled'
    REFUND = 'refund'


class PaymentMode(models.TextChoices):
    """
    The PaymentMode class represents the different modes a payment can be made with.

    It's a subclass of Django's TextChoices, which allows for easier creation of choices for a CharField.

    Choices:
    CASH: The payment was made with cash.
    CARD: The payment was made with a card.
    BANK: The payment was made through a bank transfer.
    """
    CASH = 'cash'
    CARD = 'card'
    BANK = 'bank'


class Payment(ActivityLogger):
    """
    The Payment model represents a payment made for an order.

    Each Payment has a one-to-one relationship with the Order model,
    which represents the order the payment is for.

    Fields:
    order: The order the payment is for. It's a one-to-one field relating to the Order model.
    status: The status of the payment. It's a char field with choices defined by the PaymentStatus class.
    method: The method used for the payment. It's a char field with choices defined by the PaymentMode class.

    Inherits from:
    ActivityLogger: An abstract model that adds created and updated fields to the model.
    """
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, choices=PaymentStatus.choices, default=PaymentStatus.PENDING)
    method = models.CharField(max_length=50, choices=PaymentMode.choices, default=PaymentMode.CARD)