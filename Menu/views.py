from rest_framework import generics
from .models import MenuItem, Category, MenuItemCategory
from .serializers import MenuItemSerializer, CategorySerializer, MenuItemCategorySerializer


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
