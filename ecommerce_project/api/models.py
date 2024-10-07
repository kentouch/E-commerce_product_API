from django.db import models

# Create your models here.
# Each product should have the following attributes: 
# Name, Description, Price, Category, Stock Quantity, Image URL, and Created Date



# Each product should be associated with a category for better organization
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
# let's create a Product model
# it should have the following attributes: Name, Description, Price, Category, Stock Quantity, Image URL, and Created Date
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    stock_quantity = models.IntegerField()
    image_url = models.URLField()
    created_date = models.DateTimeField(auto_now_add=True)  # Add the created_date field

    def __str__(self):
        return self.name
