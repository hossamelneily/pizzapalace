from django.urls import path

from .views import (
    MenuItemListCreateAPIView,
    MenuItemRetrieveUpdateDestroyAPIView,
    CategoryListCreateAPIView,
    CategoryRetrieveUpdateDestroyAPIView,
    MenuItemCategoryListCreateAPIView,
    MenuItemCategoryRetrieveUpdateDestroyAPIView
)


urlpatterns = [
    path('menu-items/', MenuItemListCreateAPIView.as_view(), name='menu-item-list-create'),
    path('menu-items/<int:pk>/', MenuItemRetrieveUpdateDestroyAPIView.as_view(), name='menu-item-detail'),
    path('categories/', CategoryListCreateAPIView.as_view(), name='category-list-create'),
    path('categories/<int:pk>/', CategoryRetrieveUpdateDestroyAPIView.as_view(), name='category-detail'),
    path('menu-item-categories/', MenuItemCategoryListCreateAPIView.as_view(), name='menu-item-category-list-create'),
    path('menu-item-categories/<int:pk>/', MenuItemCategoryRetrieveUpdateDestroyAPIView.as_view(), name='menu-item-category-detail'),
]