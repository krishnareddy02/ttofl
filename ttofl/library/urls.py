from django.urls import path
from .import views

urlpatterns=[
    path('index',views.index,name="index"),
    path('',views.home,name="home"),
    path('home_page',views.home_page,name="home_page"),
    path('registration',views.registration,name="registration"),
    path('book_details',views.book_details,name="book_details"),
    path('login_page',views.login_page,name="login_page"),
    path('login',views.login,name="login"),
    path('login_page',views.login_page,name="login_page"),
    path('logout',views.logout,name="logout"),
    path('admin',views.admin,name="admin"),
    path('admin_login',views.admin_login,name="admin_login"),
]
