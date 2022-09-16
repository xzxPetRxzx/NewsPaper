
from django.shortcuts import render
from django.views import View
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView, TemplateView
from .models import Post, Author, User, Category, PostCategory
from .filters import PostFilter
from .forms import PostForm
from django.shortcuts import redirect
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=Post)
def send_for_subscribers(sender, instance, **kwargs):
    html_content = render_to_string(
        'mail_to_subscribers.html',
        {
         'post': instance
        }

    )

    subscribers = User.objects.filter(category__post = instance.id).values('email')
    #не могу получить список подписчиков он почему то получается пустым
    #хотя если уменьшить на 1 значение instanse.id все работает

    subject = f'Здравствуте . Новая статья в вашем любимом разделе{subscribers}'
    msg = EmailMultiAlternatives(
        subject=subject,
        to=['garamet1989@yandex.ru']
    )
    msg.attach_alternative(html_content, "text/html")
    msg.send()




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


class CathegoryPostList(ListView):
    model = Post
    ordering = 'creation_date'
    template_name = 'post_list_cat.html'
    context_object_name = 'posts'
    ordering = '-creation_date'
    paginate_by = 10
    form_class = PostForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cat_name'] = Post.objects.filter(category__id=self.kwargs['cat_id']).values('category__name').first()['category__name']
        context['category_id'] = self.kwargs['cat_id']
        cur_user = self.request.user
        context['is_not_subscriber'] = not Category.objects.filter(id = self.kwargs['cat_id']).filter(subscribers = cur_user).exists()
        return context

    def get_queryset(self):
        return Post.objects.filter(category__id=self.kwargs['cat_id'])


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

class UserView(LoginRequiredMixin, TemplateView):
    template_name = 'user_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_not_author'] = not self.request.user.groups.filter(name='authors').exists()
        return context

@login_required
def upgrade_me(request):
    author_group = Group.objects.get(name='authors')
    if not request.user.groups.filter(name='authors').exists():
        author_group.user_set.add(request.user)
        Author.objects.create(user = request.user)
    return redirect('/news/userpage')

@login_required
def subscribe_me(request):
    cur_user = request.user
    id_cat = request.GET.get('category')
    if not Category.objects.filter(id = request.GET.get('category')).filter(subscribers = cur_user).exists():
        cur_cat = Category.objects.get(id = request.GET.get('category'))
        cur_cat.subscribers.add(cur_user)
    return redirect(f'/news/cathegory/{id_cat}')

