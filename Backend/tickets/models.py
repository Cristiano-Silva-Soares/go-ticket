from django.db import models


class TicketType(models.Model):
    name = models.CharField(max_length=100)

    price = models.DecimalField(
        max_digits=8,
        decimal_places=2
    )

    description = models.TextField(blank=True)

    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} - {self.price}"


class VisitSlot(models.Model):
    date = models.DateField()

    start_time = models.TimeField()

    end_time = models.TimeField()

    max_capacity = models.PositiveIntegerField()

    sold_tickets = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.date} {self.start_time}-{self.end_time}"
