from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

# 리스트를 출력하는 django 기본 라이브러리
class PostList(ListView):
    model = Post
    ordering = '-pk'                   

# 하나의 리스트를 불러오는 django 기본 라이브러리
class PostDetail(DetailView):
    model = Post