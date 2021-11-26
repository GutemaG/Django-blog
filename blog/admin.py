from django.contrib import admin
from .models import Tag, Blog, Category, Comment, Like,Bookmark
# Register your models here.

admin.site.register([Tag, Blog, Category, Comment, Like,Bookmark])
