from rest_framework import serializers
from .models import Order, OrderItem
from django.contrib.auth.models import AnonymousUser


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['id', 'menu_item', 'quantity']


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ['id', 'user', 'status', 'created_at', 'total_price', 'delivery_time', 'items']

    def create(self, validated_data):
        user = self.context['request'].user
        items_data = validated_data.pop('items')
        if isinstance(user, AnonymousUser):
            validated_data['user'] = None
        order = Order.objects.create(**validated_data)
        for item_data in items_data:
            OrderItem.objects.create(order=order, **item_data)
        return order
