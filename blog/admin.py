from django.contrib import admin
from .models import Tag, Blog, Category, Comment, Like
# Register your models here.

admin.site.register([Tag, Blog, Category, Comment, Like])
