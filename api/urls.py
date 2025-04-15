from django.urls import path
from . import views
from .views import PostListCreateView

urlpatterns = [
    path('create/', views.create_post, name='create_post'),
    path('posts/', PostListCreateView.as_view(), name='post-list-create'),
]
