from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

class PostList(ListView):
    model = Post
    ordering = 'creation_date'
    template_name = 'post_list.html'
    context_object_name = 'posts'

class PostDetails(DetailView):

    model = Post
    template_name = 'post.html'
    context_object_name = 'cur_post'
# Create your views here.
