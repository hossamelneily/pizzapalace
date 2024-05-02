from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import OrderItem
from django.db.models import Sum, F
from django.utils import timezone


@receiver([post_save, post_delete], sender=OrderItem)
def update_order_total_price(sender, instance, **kwargs):
    """
    Signal receiver function to update the total price of the order
    """
    order = instance.order
    total_price = order.items.aggregate(total_price=Sum(F('menu_item__price')
                                                        * F('quantity')))['total_price'] or 0
    order.total_price = total_price
    order.save()


@receiver([post_save, post_delete], sender=OrderItem)
def update_order_status_and_delivery_time(sender, instance, **kwargs):
    """Update the order status and delivery"""
    order = instance.order
    all_items_completed = order.items.filter(status='completed').count() == order.items.count()
    if all_items_completed and order.status != 'completed':
        order.status = 'completed'
        order.delivery_time = timezone.now() - order.created_at
        order.save()
