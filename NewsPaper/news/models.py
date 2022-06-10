from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)

    @staticmethod
    def update_rating(r_user):
        def summ(a):
            s = 0
            for i in a:
                s += i.get('rating')
            return s
        r_auth = Author.objects.get(user__id = r_user.id)
        r_post = summ(Post.objects.filter(author = r_auth.id).values('rating'))
        r_comm = summ(Comment.objects.filter(user = r_user.id).values('rating'))
        r_aut_comm = summ(Comment.objects.filter(post__author = r_auth.id).values('rating'))
        r_auth.rating = r_post * 3 + r_comm + r_aut_comm
        r_auth.save()

class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)

class Post(models.Model):
    article = 'ar'
    news = 'nw'
    TYPE_CHOISES = ((article, 'Статья'), (news, 'Новости'))
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    type = models.CharField(max_length=9, choices=TYPE_CHOISES, default= article)
    category = models.ManyToManyField(Category, through='PostCategory')
    creation_date = models.DateTimeField(auto_now_add=True)
    heading = models.CharField(max_length=255)
    content = models.TextField()
    rating = models.IntegerField(default=0)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def preview(self):
        text = self.content[:128]+'...'
        return text
    def __str__(self):
        return f'Заголовок: {self.heading}, Дата размещения: {self.creation_date}, Текст: {self.content[:20]}'

    def get_absolute_url(self):
        return f'/news/{self.id}'


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

# Create your models here.
