from django.contrib import admin

from order.models import Order, ExchangeRate

admin.site.register(Order)
admin.site.register(ExchangeRate)
