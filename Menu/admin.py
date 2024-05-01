from django.contrib import admin

from .models import MenuItem, Category, MenuItemCategory

admin.site.register(MenuItem)
admin.site.register(Category)
admin.site.register(MenuItemCategory)
