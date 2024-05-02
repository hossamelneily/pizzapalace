from celery.exceptions import CeleryError
from django.db import transaction
from rest_framework import generics
from .models import Order
from .serializers import OrderSerializer
from .tasks import cook_pizza
import logging

logger = logging.getLogger(__name__)


class OrderListCreateView(generics.ListCreateAPIView):
    serializer_class = OrderSerializer

    def get_queryset(self):
        return Order.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        order_instance = serializer.instance
        order_instance.status = 'in_progress'
        order_instance.save()
        pizzas = order_instance.items.filter(menu_item__menuitemcategory__category__name='pizza')
        # side_dishes = order_instance.items.filter(menu_item__menuitemcategory__category__name='side_dish')
        # toppings = order_instance.items.filter(menu_item__menuitemcategory__category__name='topping')

        if pizzas.exists():
            try:
                for pizza in pizzas.all():
                    pizza.status = 'in_progress'
                    pizza.save()
                    cook_pizza.delay(pizza.id)
            except CeleryError as e:
                logger.error(f"Failed to enqueue cook_pizza task for order ID {pizza.order.id}: {e}")
                # we can send emails here to notify the admin
            except Exception as e:
                logger.error(f"Unexpected error occurred: {e}")


class OrderRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
