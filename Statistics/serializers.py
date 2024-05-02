from rest_framework import serializers
from .models import OrderStatistics


class OrderStatisticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderStatistics
        fields = '__all__'
