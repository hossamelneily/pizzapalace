from rest_framework import generics
from .models import MenuItem, Category, MenuItemCategory
from .serializers import MenuItemSerializer, CategorySerializer, MenuItemCategorySerializer
from django.contrib.admin.views.decorators import user_passes_test


class MenuItemListCreateAPIView(generics.ListCreateAPIView):
    """ List and create menu item """
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer


class MenuItemRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    """ Retrieving, updating, and deleting a specific menu item """
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer


class CategoryListCreateAPIView(generics.ListCreateAPIView):
    """ List and create category """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    """ Retrieving, updating, and deleting a specific category """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class MenuItemCategoryListCreateAPIView(generics.ListCreateAPIView):
    """ List and create item-category associations """
    queryset = MenuItemCategory.objects.all()
    serializer_class = MenuItemCategorySerializer


class MenuItemCategoryRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    """ Retrieve, update, and delete a specific item-category association """
    queryset = MenuItemCategory.objects.all()
    serializer_class = MenuItemCategorySerializer


def admin_required(function):
    """ Decorator for views that checks if the user is an admin """
    actual_decorator = user_passes_test(
        lambda user: user.is_superuser,
        login_url='/admin/login/',
        redirect_field_name=None
    )
    return actual_decorator(function)
