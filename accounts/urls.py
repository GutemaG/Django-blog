from django.urls import path

from . import views

urlpatterns = [
    path('login/',views.loginPage,name="login"),
    path('register/',views.registerPage,name="register"),
    path('logout/',views.logoutUser,name="logout"),
    path('profile/',views.profile,name="profile"),
    path('user-account-detail/<int:pk>',views.user_account_detail,name="user-account-detail"),

]
