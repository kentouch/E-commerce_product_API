from .models import Product, CustomUser
from rest_framework.permissions import BasePermission

# let's make sure only admin can create, update or delete products
# if the user is not admin then he can only see the products
class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True
        return request.user.is_staff
    