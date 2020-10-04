from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    CreateAPIView,
    UpdateAPIView,
    DestroyAPIView
)


from rest_framework.permissions import AllowAny, IsAuthenticated
from django.shortcuts import render
from .models import Author, Post
from .serializers import PostSerializer

class PostListView(ListAPIView):
    permission_classes = (AllowAny, )
    serializer_class = PostSerializer
    queryset = Post.objects.all()
