from .views import ProductListCreateView, ProductDetailView, CategoryListCreateView
from django.urls import path

urlpatterns = [
    path('', CategoryListCreateView.as_view(), name = 'category-list-create'),
    path('product/', ProductListCreateView.as_view(), name='product-list-create'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
]