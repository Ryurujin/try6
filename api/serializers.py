from rest_framework import serializers
from app.models import *

#user
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModelsUser
        fields = ('id', 'username', 'password', 'image', )

#category
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ModelsCategory
        fields = '__all__'

#post
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModelsPost
        fields = '__all__'

