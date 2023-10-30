from django.urls import path

from . import views

urlpatterns = [
  path('', views.index, name='posts'),     #www.ryan-blogs.com\posts\
  path('<int:post_id>', views.post, name='post'), #www.ryan-blogs.com\posts\<id>
  path('search', views.search, name='search') #www.ryan-blogs.com\posts\search
]