from django.shortcuts import render
from .models import Post
from .serializers import PostSerializer
from rest_framework import generics
# Create your views here.

class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer