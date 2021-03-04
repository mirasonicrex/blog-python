from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('posts/', views.posts_index, name='posts_index'),
    path('posts/<int:post_id>/', views.posts_detail, name='posts_detail'),
    path('posts/create/', views.PostCreate.as_view(), name='posts_create'),
    path('posts/<int:pk>/update', views.PostUpdate.as_view(), name='posts_update'),
    path('posts/<int:pk>/delete', views.PostDelete.as_view(), name='posts_delete'),
    path('accounts/signup/', views.signup, name='signup'),
    path('posts/<int:post_id>/add_comment/',
         views.add_comment, name='add_comment'),
    path('comments/<int:pk>/update/',
         views.CommentUpdate.as_view(), name='comments_update'),
    path('comments/<int:pk>/delete/',
         views.CommentDelete.as_view(), name='comments_delete'),
]
