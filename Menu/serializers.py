from rest_framework import serializers
from .models import MenuItem, Category, MenuItemCategory


class MenuItemSerializer(serializers.ModelSerializer):
    """Serializer for Menu Item model"""
    class Meta:
        model = MenuItem
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    """Serializer for Category model"""
    class Meta:
        model = Category
        fields = ['id', 'name', 'description']


class MenuItemCategorySerializer(serializers.ModelSerializer):
    """Serializer for MenuItemCategory model"""
    class Meta:
        model = MenuItemCategory
        fields = ['id', 'menu_item', 'category']
