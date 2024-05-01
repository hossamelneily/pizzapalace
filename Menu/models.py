from django.db import models


class MenuItem(models.Model):
    """Menu Item Model"""
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    allergens = models.CharField(max_length=200, blank=True)
    dietary_restrictions = models.CharField(max_length=200, blank=True)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    """category model """
    CATEGORY_NAMES = (
        ('pizza', 'Pizza'),
        ('side_dish', 'SideDish'),
        ('drink', 'Drink'),
        ('topping', 'Topping'),
    )
    name = models.CharField(max_length=100, choices=CATEGORY_NAMES)
    description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class MenuItemCategory(models.Model):
    """Associated model for menu item category"""
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.menu_item.name} - {self.category.name}"

    class Meta:
        verbose_name = "MenuItem Category"
        verbose_name_plural = "MenuItem Categories"
