from django.db import models
from django.conf import settings

from tickets.models import TicketType


class Sale(models.Model):
    ticket_type = models.ForeignKey(
        TicketType,
        on_delete=models.PROTECT
    )

    attendant = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT
    )

    quantity = models.PositiveIntegerField(default=1)

    unit_price = models.DecimalField(
        max_digits=8,
        decimal_places=2
    )

    total_price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.unit_price = self.ticket_type.price
        self.total_price = self.unit_price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Sale #{self.id}"
