from django.urls import path
from .views import PostList, PostDetails

urlpatterns = [

   path('', PostList.as_view()),
   path('<int:pk>', PostDetails.as_view()),
]