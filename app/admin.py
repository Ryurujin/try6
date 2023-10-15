from django.contrib import admin
from .models import *

#user
@admin.register(ModelsUser)
class UserAdmin(admin.ModelAdmin):
    username = ('id', 'title')
    username_links = ('id', 'title')

#category
@admin.register(ModelsCategory)
class CategoryAdmin(admin.ModelAdmin):
    username = ('id', 'title')
    username_links = ('id', 'title')

#post
@admin.register(ModelsPost)
class PostAdmin(admin.ModelAdmin):
    username = ('id', 'title')
    username_links = ('id', 'title')
    
