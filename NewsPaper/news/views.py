from django.shortcuts import render
from django.views import View
from django.core.paginator import Paginator

from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from .models import Post, Author, User
from .filters import PostFilter
from .forms import PostForm


class PostList(ListView):
    model = Post
    ordering = 'creation_date'
    template_name = 'post_list.html'
    context_object_name = 'posts'
    ordering = '-creation_date'
    paginate_by = 10
    form_class = PostForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())

        context['form'] = PostForm
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()

        return super().get(request, *args, **kwargs)


class PostDetails(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'cur_post'


# Create your views here.



class PostCreate(CreateView):
    template_name = 'post_add.html'
    form_class = PostForm
    success_url = '/news/'

class PostUpdate(UpdateView):
    template_name = 'post_add.html'
    form_class = PostForm
    success_url = '/news/'

    # метод get_object мы используем вместо queryset, чтобы получить информацию об объекте, который мы собираемся редактировать
    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)


# дженерик для удаления товара
class PostDelete(DeleteView):
    template_name = 'post_delete.html'
    queryset = Post.objects.all()
    success_url = '/news/'
