from .views import ProductList, ProductDetail
from django.urls import path

urlpatterns = [
    path('', ProductList.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductDetail.as_view(), name='product-detail'),
]