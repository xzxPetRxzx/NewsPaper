from django.urls import path
from .views import CathegoryPostList, PostList, PostDetails, PostDelete, PostUpdate, PostCreate, UserView, upgrade_me, subscribe_me
from django.views.decorators.cache import cache_page
urlpatterns = [
    path('', PostList.as_view()),
    path('search', PostList.as_view(template_name = 'post_list_filter.html', paginate_by = False)),
    path('add/', PostCreate.as_view()),
    path('<int:pk>',PostDetails.as_view()),
    path('<int:pk>/edit/', PostUpdate.as_view()),
    path('<int:pk>/delete/', PostDelete.as_view()),
    path('userpage', UserView.as_view()),
    path('userpage/upgrade', upgrade_me, name = 'upgrade'),
    path('cathegory/<int:cat_id>', CathegoryPostList.as_view(), name = 'cathegory'),
    path('cathegory/subscribe', subscribe_me),
    ]