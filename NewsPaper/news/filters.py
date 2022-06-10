from django_filters import FilterSet
from .models import Post

class PostFilter(FilterSet):
    class Meta:
        model = Post
        fields = {'creation_date': ['gt'],
                  'heading': ['icontains'],
                  'author__user__username': ['icontains']
        }
