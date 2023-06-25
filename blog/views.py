from django.shortcuts import render
from .models import Post


def index(request):
    # 기본키 역순으로 출력하기
    posts = Post.objects.all().order_by('-pk')

    return render(
        request,
        'blog/index.html',
        {
            'posts': posts,
        }
    )
