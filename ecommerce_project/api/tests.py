#from typing import Any
#from django.test import TestCase
from rest_framework import status, test
from rest_framework.authtoken.models import Token
from django.urls import reverse
from .models import Product, Category
from django.contrib.auth import get_user_model
from unittest.mock import patch

class BookAPITest(test.APITestCase):
    
    # Let's write a Set up function for the tests
    def setUp(self):
        # let's first delete all the products before creating new ones
        Product.objects.all().delete()

        # let's reference our CustomUser model
        User = get_user_model()

        # let's first create a user and authenticate him
        self.user = User.objects.create_user(email='7rOJW@example.com', username='testuser', password='testpassword')
        self.client.force_authenticate(user=self.user)
        #self.token = Token.objects.create(user=self.user)
        # let's Configure a separate test database to avoid impacting your production or development data
        #self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)  # or self.client.force_authenticate(username='testuser', password='testpassword')
        
        # create a category instance before running the product tests
        self.category = Category.objects.create(name="Accessories")
        # Set up initial data
        # Create two products
        self.product1 = Product.objects.create(name="Product 1", description="This is a product", price=10, category=self.category, stock_quantity=10, image_url="https://example.com/product1.png", created_date=2022-1-1)
        self.product2 = Product.objects.create(name="Product 2",description="This is another product", price=20, category=self.category, stock_quantity=10, image_url="https://example.com/product2.png", created_date=2022-1-5)

    ###  Test to retrieve the list of products
    def test_get_products(self):
        
        # URL for the API endpoint
        url = reverse('product-list-create')  # Assuming the URL is named 'product-list'
        
        # Simulate a GET request
        response = self.client.get(url)
        
        
        # Check that the request succeeded
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 2 )
         # Check the returned data
        #self.assertEqual(len(response.data), 2)  # Expecting 2 products
        self.assertEqual(response.data['results'][0]['price'], 10)
        self.assertEqual(response.data['results'][1]['price'], 20)
    
    """ def tearDown(self):
        return Product.objects.all().delete()"""


    ###  Test to retrieve a single product
    def test_get_product(self):
     
        # URL for the API endpoint to retrieve a single product
        # args = [1] represents the ID of the product you want to retrieve
        url = reverse('product-detail', kwargs={'pk': self.product1.id})
        
        # Simulate a GET request
        response = self.client.get(url)
        
        # Check that the request succeeded
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # Check the returned data
        self.assertEqual(response.data['name'], "Product 1")
        self.assertEqual(response.data['category'], self.category.id)
        self.assertEqual(response.data['price'], 10)
    
      ### Test to create a new product
    def test_create_product(self):
       
        url = reverse('product-list-create')
        data = {
            "name" : "New product",
            "description"  : "This is another product", 
            "price" : 35, 
            "category" : self.category.id, 
            "stock_quantity" : 11, 
            "image_url" : "https://example.com/product2.png", 
            "created_date" : 2022-1-7 
        }
        
        # Simulate a POST request
        response = self.client.post(url, data, format='json')

    # Check that the request succeeded
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # Check the returned data
        self.assertEqual(response.data['name'], "New product")
        self.assertEqual(response.data['description'], "This is another product")
        self.assertEqual(response.data['price'], 35)
    
    ### Test to update an existing product
    # from unittest.mock import patch for patching permission_classes
   
    # patching permission_classes
    @patch('api.views.ProductDetailView.permission_classes', [])
    def test_update_product(self):

        # url for the API endpoint to update a product 
        url = reverse('product-detail', kwargs={'pk': self.product2.id})
        data = {
            "name" : "Product updated",
            "description"  : "This is product updated", 
            "price" : 25, 
            "category" : self.category.id, 
            "stock_quantity" : 30, 
            "image_url" : "https://example.com/product_updated.png", 
            "created_date" : 2022-1-8 
        }
        
        # Simulate a PUT request
        response = self.client.put(url, data, format='json')
        
        # Check that the request succeeded
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Check the returned data
        self.assertEqual(response.data['name'], "Product updated")
        self.assertEqual(response.data['description'], 'This is product updated')
        self.assertEqual(response.data['stock_quantity'], 30)

    ### Test to delete an existing product

    # let's patch permission_classes
    @patch('api.views.ProductDetailView.permission_classes', [])
    def test_delete_product(self):
   
        # URL for the API endpoint to delete a book with Id = 1
        url = reverse('product-detail', kwargs={'pk': self.product1.pk})
        
        # Simulate a DELETE request
        response = self.client.delete(url)
        
        # Check that the request succeeded
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # check that the book is deleted
        self.assertEqual(Product.objects.count(), 1)


    ### Test category list and its creation

    # list all categories
    def test_list_category(self):

        # url for the API endpoint to list categories
        url = reverse('category-list-create')
        # Simulate a get request 
        response = self.client.get(url) 
        # checking if the request is succeeding 
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_category(self):
        # url for the API endpoint to create a category
        url = reverse('category-list-create')
        # enter category data
        data = {
                'name': 'Electronics'
        }
        
        response = self.client.post(url, data, format='json')
        # let's see if the creation process succeeded
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)