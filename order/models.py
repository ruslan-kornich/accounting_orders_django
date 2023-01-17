from django.db import models


class Order(models.Model):
    excel_id = models.PositiveSmallIntegerField(db_index=True, )
    order_id = models.CharField(db_index=True, max_length=10)
    price_usd = models.DecimalField(max_digits=9, decimal_places=2)
    price_uah = models.DecimalField(max_digits=9, decimal_places=2)
    delivery_date = models.DateField()
    msg_status = models.BooleanField(default=False)
    msg_status_text = models.CharField(max_length=20, default='In_process...')

    class Meta:
        ordering = ('excel_id',)

    def __str__(self):
        return f"{self.order_id} {self.excel_id}"


class ExchangeRate(models.Model):
    from_code = models.PositiveSmallIntegerField(default=840)
    to_code = models.PositiveSmallIntegerField(default=980)
    rate = models.DecimalField(max_digits=6, decimal_places=2, default=1.0)
    date_of_rate = models.CharField(max_length=30, null=True, blank=True)
