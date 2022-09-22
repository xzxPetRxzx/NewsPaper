from datetime import date, timedelta

from celery import shared_task

from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from .models import Post, User, Category



def collect_subscribers_email_for_category(category_id):
    emails = []
    sub_mails = list(User.objects.filter(category=category_id).values_list('email'))
    for mail in sub_mails:
        emails.append(mail[0])
    return emails

def collect_categories():
    categories = []
    sub_categories = list(Category.objects.all().values_list('id'))
    for category in sub_categories:
        categories.append(category[0])
    return categories

def collect_categories_for_post(post_id):
    categories = []
    sub_categories = list(Category.objects.filter(post=post_id).values_list('id'))
    for category in sub_categories:
        categories.append(category[0])
    return categories

@shared_task
def mail_to_subscribers(post_id):
    new_post = Post.objects.get(pk = post_id)

    html_content = render_to_string(
        'mail_to_subscribers.html',
        {
            'post': new_post
        }
    )

    for category in collect_categories_for_post(post_id):
        for email in collect_subscribers_email_for_category(category):
            subject = f'Здравствуте . Новая статья в вашем любимом разделе {Category.objects.get(pk = category).name}'
            msg = EmailMultiAlternatives(
                subject=subject,
                to=[str(email)]
            )
            msg.attach_alternative(html_content, "text/html")
            msg.send()

@shared_task
def week_info_mail():
    posts = Post.objects.filter(creation_date__gte = (date.today() - timedelta(days=7)))

    html_content = render_to_string(
        'week_mail.html',
        {
            'posts': posts
        }
    )
    for category in collect_categories():
        for email in collect_subscribers_email_for_category(category):
            subject = f'Здравствуте . Обновление в категории {Category.objects.get(pk = category).name} за неделю'
            msg = EmailMultiAlternatives(
                subject=subject,
                to=[str(email)]
            )
            msg.attach_alternative(html_content, "text/html")
            msg.send()
