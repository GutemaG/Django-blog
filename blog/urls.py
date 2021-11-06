
from django.urls import path
# from django.urls.conf import include
from . import views

urlpatterns = [
    path('', views.home,name='home'),
    path('blogs', views.blogs,name='blogs'),
    path('read_blog/<int:pk>', views.read_blog,name='read-blog'),
    path('add_blog/', views.add_blog,name='add-blog'),
    path('about', views.about,name='about'),
]