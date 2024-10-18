# Importing Serializer
from rest_framework import serializers
from .models import Product, Category

# Product Serializer
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    # validation for name, price, and stock_quantity
    def validate(self, data):
        if data['name'] == data['description']:
            raise serializers.ValidationError("Name and Description cannot be same")
        if data['price'] <= 0:
            raise serializers.ValidationError("Price cannot be zero")
        # Make sure the Stock Quantity is automatically reduced when an order 
        # is placed (future enhancement or consider as optional for now)
        if data['stock_quantity'] <= 0:
            raise serializers.ValidationError("Stock Quantity cannot be zero")
        return data 

# Category Serializer
class CategorySerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=100)
    product = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = Category  
        fields = ['name', 'product']