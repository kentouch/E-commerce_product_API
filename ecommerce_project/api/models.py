from django.db import models

# Create your models here.
# Each product should have the following attributes: 
# Name, Description, Price, Category, Stock Quantity, Image URL, and Created Date

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField()
    category = models.CharField(max_length=100)
    stock_quantity = models.IntegerField()
    image_url = models.URLField()
    created_date = models.DateTimeField(auto_now_add=True)  # Add the created_date field

    def __str__(self):
        return self.name