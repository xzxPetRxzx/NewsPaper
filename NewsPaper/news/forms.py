from typing import Dict

from django.forms import ModelForm, HiddenInput
from .models import Post, Author, User, Category
from allauth.account.forms import SignupForm
from django.contrib.auth.models import Group


# Создаём модельную форму
class PostForm(ModelForm):

    class Meta:
        model = Post
        fields = ('heading', 'content', 'type', 'author', 'category')
        #widgets = {'author': HiddenInput()}
        labels = dict(heading=('Заголовок'), content=('Содержание'), type=('Тип'), category=('Категория'))



class CommonSignupForm(SignupForm):

    def save(self, request):
        user = super(CommonSignupForm, self).save(request)
        basic_group = Group.objects.get(name='common')
        basic_group.user_set.add(user)
        return user