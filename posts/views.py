from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q

from .models import Post

def index(request):
  posts_list = Post.objects.order_by('-post_date').filter(is_published = True)

  paginator = Paginator(posts_list, 6)
  page = request.GET.get('page')
  paged_posts_list = paginator.get_page(page)

  context = {
    'posts': paged_posts_list
  }
  
  return render(request, 'posts/posts.html', context)

def post(request, post_id:int):
  post = get_object_or_404(Post, pk=post_id)

  context = {
    'post': post
  }
    
  return render(request, 'posts/post.html', context)

def search(request):
  posts = Post.objects.order_by('-post_date').filter(is_published = True)

  if 'search_text' in request.GET:
    search_text = request.GET['search_text']

    if search_text:
      posts = posts.filter(Q(title__icontains=search_text)
                           | Q(text__icontains=search_text)
                           | Q(blogger__name__icontains=search_text))

  context = {
    'posts': posts
  }
  
  return render(request, 'posts/search.html', context)