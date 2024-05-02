from django.db.models import Count, Sum, Avg

from rest_framework.response import Response
from rest_framework.views import APIView

from Orders.models import Order, OrderItem


class OrderStatisticsAPIView(APIView):
    def get(self, request):
        start_date = request.query_params.get('start_date')
        end_date = request.query_params.get('end_date')
        orders = Order.objects.filter(created_at__range=(start_date, end_date))

        total_orders = orders.count()
        total_sales = orders.aggregate(total_sales=Sum('total_price'))['total_sales'] or 0.00
        most_ordered_item = OrderItem.objects.filter(order__in=orders).values('menu_item__name').annotate(
            count=Count('menu_item')).order_by('-count').first()
        top_customer = orders.values('user__username').annotate(total_orders=Count('id')).order_by(
            '-total_orders').first()
        average_order_value = orders.aggregate(average_order_value=Avg('total_price'))['average_order_value'] or 0.00
        response_data = {
            'date_range': {'start_date': start_date, 'end_date': end_date},
            'total_orders': total_orders,
            'total_sales': total_sales,
            'most_ordered_item': most_ordered_item,
            'top_customer': top_customer,
            'average_order_value': average_order_value
        }

        return Response(response_data)


