from rest_framework import generics
from blog.models import Post
from .serializers import PostSerializer


# List all posts / Create a new post
class PostListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


# Retrieve / Update / Delete a single post
class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
