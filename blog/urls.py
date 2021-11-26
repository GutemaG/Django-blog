
from django.urls import path
# from django.urls.conf import include
from . import views

urlpatterns = [
    path('', views.home,name='home'),
    path('blogs/<str:tag>', views.blogs,name='blogs'),
    path('blog/edit/<int:pk>', views.edit_blog,name='edit-blog'),
    path('read_blog/<int:pk>', views.read_blog,name='read-blog'),
    path('about', views.about,name='about'),
    path('create-blog', views.create_blog,name='create-blog'),
    path('add-comment/<int:pk>', views.add_comment,name='add-comment'),
    path('my-blog', views.auth_user_blog,name='auth-user-blog'),
    path('like/<int:pk>', views.like_blog,name='like-blog'),
    # path('blog/bookmark/<int:pk>', views.bookmark,name='bookmark'),
    # path('blog/auth-user-bookmark',views.auth_user_bookmark,name='bookmarked')
    # path('blog/bookmarked', views.auth_user_bookmark,name='bookmarked'),
]
    # path('add_blog/', views.add_blog,name='add-blog'),