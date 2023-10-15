from rest_framework.permissions import BasePermission

#user
class UserPermission(BasePermission):
    def has_permission(self, request, view):

        if request.method == 'GET':
            return request.user.is_staff

        elif request.method == 'POST':
            return request.user.is_authenticated
        
class UserDetailPermission(BasePermission):
    def has_permission(self, request, view):

        if request.method in ['GET', 'PUT', 'DELETE']:
            return request.user.is_authenticated
        
#category
class CategoryPermission(BasePermission):
    def has_permission(self, request, view):

        if request.method == 'GET':
            return True
        
        elif request.method == 'POST':
            return request.user.is_authenticated

class CategoryDetailPermission(BasePermission):
    def has_permission(self, request, view):

        if request.method in ['PUT', 'DELETE']:
            return request.user.is_authenticated
        
        elif request.method == ['GET']:
            return True
        
#post
class PostPermission(BasePermission):
    def has_permission(self, request, view):

        if request.method in ['GET', 'POST']:
            return request.user.is_authenticated
        

class PostDetailPermission(BasePermission):
    def has_permission(self, request, view):

        if request.method in ['GET', 'PUT', 'DELETE']:
            return request.user.is_authenticated
        