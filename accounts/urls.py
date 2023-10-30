from django.urls import path

from . import views

urlpatterns = [
  path('login', views.login, name='login'),     #www.ryan-blogs.com\accounts\login
  path('register', views.register, name='register'), #www.ryan-blogs.com\accounts\register
  path('logout', views.logout, name='logout') #www.ryan-blogs.com\accounts\logout
]