from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

# 리스트를 출력하는 django 기본 라이브러리
# index함수 대신 사용
class PostList(ListView):
    model = Post
    ordering = '-pk'                    # 기본키 역순으로 출력
    # template_name = 'blog/index.html'   #기본 post_list.html 이름으로 사용 --> 경로지정 가능

# 하나의 리스트를 불러오는 django 기본 라이브러리
# single_post_page함수 대신 사용
class PostDetail(DetailView):
    model = Post

# def index(request):
#     # 기본키 역순으로 출력하기
#     posts = Post.objects.all().order_by('-pk')

#     return render(
#         request,
#         'blog/index.html',
#         {
#             'posts': posts,
#         }
#     )

# 각 고유 블로그 페이지 내용 불러오기
# def single_post_page(request, pk):
#     posts = Post.objects.get(pk=pk)

#     return render(
#         request,
#         'blog/single_page.html',
#         {
#             'post': posts,
#         }
#     )