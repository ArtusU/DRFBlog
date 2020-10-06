from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    CreateAPIView,
    UpdateAPIView,
    DestroyAPIView
)


from rest_framework.permissions import AllowAny, IsAuthenticated
from django.shortcuts import render
from django.shortcuts import render
from .models import Author, Post
from .serializers import PostSerializer, PostCreateSerializer
from django.views.decorators.csrf import csrf_exempt


def home(request):
    return render(request, 'index.html')

class PostListView(ListAPIView):
    permission_classes = (AllowAny, )
    serializer_class = PostSerializer
    queryset = Post.objects.all()


class PostCreateView(ListAPIView):
    permission_classes = (AllowAny, )
    serializer_class = PostCreateSerializer
    queryset = Post.objects.all()