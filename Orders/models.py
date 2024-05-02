from django.db import models

from django.contrib.auth.models import User

from Menu.models import MenuItem


class Order(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    delivery_time = models.DurationField(null=True, blank=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        if self.user is not None:
            return f"Order #{self.id} - {self.user.username}"
        return f"Order #{self.id} - Anonymous"


class OrderItem(models.Model):
    ITEM_STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    )
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=ITEM_STATUS_CHOICES, default='pending')
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.quantity} x {self.menu_item.name}"
