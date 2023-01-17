from rest_framework import serializers

from .models import Order


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('excel_id',
                  'order_id',
                  'price_usd',
                  'price_uah',
                  'delivery_date',
                  'msg_status_text',
                  )
