from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.
# Each product should have the following attributes: 
# Name, Description, Price, Category, Stock Quantity, Image URL, and Created Date

# Let's create a base user manager for the CustomUser model
class CustomUserManager(BaseUserManager):
    # create user function
    # it should accept username, email, password and **extra_fields
    # it should return a user object
    def create_user(self, username, email, password=None, **extra_fields):
        if not username:
            raise ValueError('The username field must be set')
        if not email:
            raise ValueError('The email field is required')
        
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    # Create superuser function
    # it should accept username, email, password and **extra_fields
    # it should return a user object
    def create_superuser(self, username, email, password=None, **extra_fields):
        # 1st step set default values for is_staff and is_superuser
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        # 2nd step check if is_staff and is_superuser are true
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(username, email, password, **extra_fields)


# Let's create a CustomUser model
# it should have the following attributes: Username, Email, Password, Is Active, Is Staff, Is Superuser
class CustomUser(AbstractBaseUser):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    # let's assign a customer manager to the CustomUser model
    objects = CustomUserManager()

    # The username field is required, so let's set it to be the email field
    # let's also set the 'username' as a required field
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.username

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
