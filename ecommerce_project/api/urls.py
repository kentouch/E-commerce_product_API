from .views import ProductList, ProductDetailView, CategoryListCreateView
from django.urls import path

urlpatterns = [
    path('', CategoryListCreateView.as_view(), name = 'category-list-create'),
    path('product/', ProductList.as_view(), name='product-list-create'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
]