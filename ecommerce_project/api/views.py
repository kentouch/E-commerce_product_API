from django.shortcuts import render
from rest_framework.pagination import PageNumberPagination
from .serializers import ProductSerializer, CategorySerializer
from .permissions import IsAdminOrReadOnly
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Product, Category
from rest_framework import generics, filters

# Create your views here.

# Category list view for more flexibility
class CategoryListCreateView(generics.ListCreateAPIView):
    # Authentication classes
    authentication_classes = [TokenAuthentication]
    # Model serializer
    serializer_class = CategorySerializer
    # set category model to the view
    def get_queryset(self):
        return Category.objects.all()


# create a pagination class
class ProductPagination(PageNumberPagination):
    # set the default page size
    page_size = 10
    # set the maximum page size
    page_size_query_param = 'page_size'
    max_page_size = 100

# Implement CRUD operations for users who will manage the products
class ProductListCreateView(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    # let's create a permission request for creating a product
    def get_permissions(self):
        if self.request.method == 'POST':
            return [IsAdminOrReadOnly()]
        return [IsAuthenticated()]
    #permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'category', 'price', 'stock_quantity' ]
    # Allow for partial matches in product names for flexible search results.
    lookup_field = 'name'
    # set pagination class
    pagination_class = ProductPagination
    # get queryset from Product model
    queryset = Product.objects.all().order_by('name')
    serializer_class = ProductSerializer

class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'category']
    # Allow for partial matches in product names for flexible search results.
    lookup_field = 'pk'

    # get queryset from Product model
    def get_queryset(self): 
        return Product.objects.all()
    
    serializer_class = ProductSerializer

    # set a reminder for when quantity is less than 0


    
      
    

