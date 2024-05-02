import time
import logging
from celery import shared_task

from Orders.models import OrderItem

logger = logging.getLogger(__name__)


@shared_task
def cook_pizza(pizza_id):
    order_item = OrderItem.objects.get(id=pizza_id)
    order_id = order_item.order_id
    pizza_name = order_item.menu_item.name

    logger.debug(f"Start cooking pizza {pizza_name} for order #{order_id}")

    prepare_dough(pizza_name, order_id)
    add_toppings(pizza_name, order_id)
    bake_pizza(pizza_name, order_id)

    order_item.status = 'completed'
    order_item.save()
    logger.debug(f"Pizza {pizza_name} cooking completed for order #{order_id}")


def prepare_dough(pizza_name, order_id):
    logger.debug(f"Preparing dough for pizza {pizza_name} for order #{order_id}")
    time.sleep(3)  # Simulate dough preparation time


def add_toppings(pizza_name, order_id):
    logger.debug(f"Adding toppings for pizza {pizza_name} for order #{order_id}")
    time.sleep(2)  # Simulate topping preparation time


def bake_pizza(pizza_name, order_id):
    logger.debug(f"Baking pizza for pizza {pizza_name} for order #{order_id}")
    time.sleep(5)  # Simulate baking time
