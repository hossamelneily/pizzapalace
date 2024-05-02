from django.urls import path
from .views import OrderStatisticsAPIView

urlpatterns = [
    path('order-statistics/', OrderStatisticsAPIView.as_view(), name='order-statistics'),
]
