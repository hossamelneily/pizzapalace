from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class OrderStatistics(models.Model):
    date = models.DateField(default=timezone.now)
    total_orders = models.IntegerField(default=0)
    total_sales = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    most_ordered_item = models.CharField(max_length=100, null=True, blank=True)
    top_customer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    average_order_value = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return f"Statistics for {self.date}"
