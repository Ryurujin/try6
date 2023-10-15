from django.urls import path, include
from .views import *

urlpatterns = [
    #user
    path('user/', User_views_list),
    path('user/<int:pk>/', User_views_detail),
    
    #category
    path('category/', Category_views_list),
    path('category/<int:pk>/', Category_views_detail),
    
    #post
    path('post/', Post_views_list),
    path('post/<int:pk>/', Post_views_detail),

    path('auth/', include('dj_rest_auth.urls')),
    
]