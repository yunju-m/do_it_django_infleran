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

# 각 고유 블로그 페이지 내용 불러오기
def single_post_page(request, pk):
    posts = Post.objects.get(pk=pk)

    return render(
        request,
        'blog/single_page.html',
        {
            'post': posts,
        }
    )