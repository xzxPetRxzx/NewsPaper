from django.urls import path
from .views import PostList, PostDetails, PostDelete, PostUpdate, PostCreate, UserView, upgrade_me

urlpatterns = [

   path('', PostList.as_view()),
   path('search', PostList.as_view(template_name = 'post_list_filter.html', paginate_by = False)),
   path('add/', PostCreate.as_view()),
   path('<int:pk>', PostDetails.as_view()),
   path('<int:pk>/edit/', PostUpdate.as_view()),
   path('<int:pk>/delete/', PostDelete.as_view()),
   path('userpage', UserView.as_view()),
   path('userpage/upgrade', upgrade_me, name = 'upgrade'),
]