from django.urls import path
from .views import PostListCreateView, PostDetailView

urlpatterns = [
    path('posts/', PostListCreateView.as_view(), name='api-post-list'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='api-post-detail'),
]
