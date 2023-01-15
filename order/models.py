from django.db import models

from django.utils import timezone


class Order(models.Model):
    id = models.IntegerField(null=False, primary_key=True, unique=True)
    order_number = models.IntegerField(null=False, default="0", unique=True)
    cost_usd = models.DecimalField(null=False, default="0", max_digits=10, decimal_places=2)
    cost_uah = models.DecimalField(null=False, default="0", max_digits=10, decimal_places=2)
    delivery_time = models.DateField(null=False, default=timezone.now)

    def __str__(self):
        return f"{self.order_number} {self.order_number}"


class DollarRate(models.Model):
    dollar = models.DecimalField(null=False, default="0", max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.dollar}"
