from django.forms import ModelForm
from .models import Post
from allauth.account.forms import SignupForm
from django.contrib.auth.models import Group


# Создаём модельную форму
class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['heading', 'content', 'type', 'author']

class CommonSignupForm(SignupForm):

    def save(self, request):
        user = super(CommonSignupForm, self).save(request)
        basic_group = Group.objects.get(name='common')
        basic_group.user_set.add(user)
        return user