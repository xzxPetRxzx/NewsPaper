from django.contrib import admin
from .models import Author, Post, PostCategory, Comment, Category
admin.site.register(Author)
admin.site.register(Post)
admin.site.register(PostCategory)
admin.site.register(Comment)
admin.site.register(Category)
# Register your models here.
