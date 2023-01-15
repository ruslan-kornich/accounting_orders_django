from django.contrib import admin

from order.models import Order, DollarRate

admin.site.register(Order)
admin.site.register(DollarRate)
