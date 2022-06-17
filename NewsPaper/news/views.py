from django.shortcuts import render
from django.views import View
from django.core.paginator import Paginator

from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView, TemplateView
from .models import Post, Author, User
from .filters import PostFilter
from .forms import PostForm
from django.shortcuts import redirect
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin



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



class PostCreate(PermissionRequiredMixin, CreateView):
    template_name = 'post_add.html'
    form_class = PostForm
    success_url = '/news/'
    permission_required = ('news.add_post')

class PostUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    template_name = 'post_add.html'
    form_class = PostForm
    success_url = '/news/'
    permission_required = ('news.change_post')

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)



class PostDelete(DeleteView):
    template_name = 'post_delete.html'
    queryset = Post.objects.all()
    success_url = '/news/'

@login_required
def upgrade_me(request):
    user = request.user
    author_group = Group.objects.get(name='authors')
    if not request.user.groups.filter(name='authors').exists():
        author_group.user_set.add(user)
    return redirect('/news')


class UserView(LoginRequiredMixin, TemplateView):
    template_name = 'user_page.html'
