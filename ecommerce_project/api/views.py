from django.shortcuts import render
from .serializers import ProductSerializer
from .permissions import IsAdminOrReadOnly
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Product
from rest_framework import generics

# Create your views here.
# Implement CRUD operations for users who will manage the products
class ProductList(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permissions_classes = [IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permissions_classes = [IsAuthenticated, IsAdminOrReadOnly]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    # set a reminder for when quantity is less than 0
    

