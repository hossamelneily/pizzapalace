from rest_framework.response import Response
from rest_framework.views import APIView

from Statistics.models import OrderStatistics
from Statistics.serializers import OrderStatisticsSerializer


class OrderStatisticsAPIView(APIView):
    def get(self, request):
        start_date = request.query_params.get('start_date')
        end_date = request.query_params.get('end_date')
        statistics = OrderStatistics.objects.filter(date__range=(start_date, end_date))

        return Response(OrderStatisticsSerializer(statistics, many=True).data)
