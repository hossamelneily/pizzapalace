import datetime

from django.db.models import Count, Sum, Avg

from Orders.models import Order, OrderItem
from Statistics.models import OrderStatistics
from celery import shared_task


@shared_task
def calculate_statistics():
    end_of_month = datetime.date.today().replace(day=1) - datetime.timedelta(days=1)
    start_of_month = end_of_month.replace(day=1)
    orders = Order.objects.filter(created_at__range=(start_of_month, end_of_month))
    total_orders = orders.count()
    total_sales = orders.aggregate(total_sales=Sum('total_price'))['total_sales'] or 0.00
    most_ordered_item = OrderItem.objects.filter(order__in=orders).values('menu_item__name').annotate(
        count=Count('menu_item')).order_by('-count').first()
    top_customer = orders.values('user__username').annotate(total_orders=Count('id')).order_by(
        '-total_orders').first()
    average_order_value = orders.aggregate(average_order_value=Avg('total_price'))['average_order_value'] or 0.00

    OrderStatistics.objects.create(
        date=end_of_month,
        total_orders=total_orders,
        total_sales=total_sales,
        most_ordered_item=most_ordered_item,
        top_customer=top_customer,
        average_order_value=average_order_value
    )
