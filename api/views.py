from django.shortcuts import render

from rest_framework.decorators import api_view, permission_classes
from rest_framework.status import *
from rest_framework.response import Response
from .permissions import *

from app.models import *
from .serializers import *

#user
@api_view(['GET', 'POST'])
@permission_classes([UserPermission])
def User_views_list(request):
    users = ModelsUser.objects.all()

    if request.method == 'GET':
        serializers =UserSerializer(users, many=True)
        return Response(serializers.data, status=HTTP_200_OK)
    
    elif request.method == 'POST':
        serializers = UserSerializer(data=request.data)

        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=HTTP_201_CREATED)
        return Response(serializers.errors, status=HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([UserDetailPermission])
def User_views_detail(request, pk):
    users = ModelsUser.objects.det(pk=pk)

    if request.method == 'GET':
        serializers = ModelsUser(users, context={'request': request})
        return Response(serializers.data, status=HTTP_200_OK)
    
    elif request.method == 'PUT':
        serializers = UserSerializer(data=request.data, context={'request': request})

        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=HTTP_201_CREATED)
        return Response(serializers.errors, status=HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        users.delete()
        return Response(status=HTTP_204_NO_CONTENT)


#category
@api_view(['GET', 'POST'])
@permission_classes([CategoryPermission])
def Category_views_list(request):
    if request.method == 'GET':
        categories = ModelsCategory.objects.all()
        serializers = CategorySerializer(categories, many=True, context={'request': request})
        return Response(serializers.data, status=HTTP_200_OK)
    
    elif request.method == 'POST':
        serializers = CategorySerializer(data=request.data, context={'request': request})

        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=HTTP_201_CREATED)
        return Response(serializers.errors, status=HTTP_400_BAD_REQUEST)
    

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([CategoryDetailPermission])
def Category_views_detail(request, pk):
    categories = ModelsCategory.object.det(pk=pk)

    if request.method == 'GET':
        serializers = CategorySerializer(categories, context={'request': request})
        return Response(serializers.data, status=HTTP_200_OK)
    
    elif request.method == 'PUT':
        serializers = CategorySerializer(categories, data=request.data)

        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=HTTP_201_CREATED)
        return Response(serializers.errors, status=HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        categories.delete()
        return Response(status=HTTP_204_NO_CONTENT)


#post
@api_view(['GET', 'POST'])
@permission_classes([PostPermission])
def Post_views_list(request, pk):
    posts = ModelsPost.objects.get(pk=pk)

    if request.method == 'GET':
        serializers = PostSerializer(posts, many=True)
        return Response(serializers.data, status=HTTP_200_OK)
    
    elif request.method == 'POST':
        serializers = PostSerializer(data=request.data)

    if serializers.is_valid():
        serializers.save()
        return Response(serializers.data, status=HTTP_201_CREATED)
    return Response(serializers.errors, status=HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([PostDetailPermission])
def Post_views_detail(request, pk):
    posts = ModelsPost.objects.get(pk=pk)

    if request.method == 'GET':
        serializers = PostSerializer(posts)
        return Response(serializers.data, status=HTTP_200_OK)
    
    elif request.method == 'PUT':
        serializers = PostSerializer(data=request.data)

        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=HTTP_201_CREATED)
        return Response(serializers.errors, status=HTTP_400_BAD_REQUEST)
    
    elif request.mrthod == 'DELETE':
        serializers.delete()
        return Response(status=HTTP_204_NO_CONTENT)
    





