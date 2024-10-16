from .views import ProductList, ProductDetailView
from django.urls import path

urlpatterns = [
    path('products/', ProductList.as_view(), name='product-list-create'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
]