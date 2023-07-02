from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post, Category

# 리스트를 출력하는 django 기본 라이브러리
class PostList(ListView):
    model = Post
    ordering = '-pk'

    def get_context_data(self, **kwargs):
        context = super(PostList, self).get_context_data()
        context['categories'] = Category.objects.all()
        context['no_category_post_count'] = Post.objects.filter(category=None).count()
        return context

# 하나의 리스트를 불러오는 django 기본 라이브러리
class PostDetail(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super(PostDetail, self).get_context_data()
        context['categories'] = Category.objects.all()
        context['no_category_post_count'] = Post.objects.filter(category=None).count()
        return context

# 카테고리별 페이지 반환 함수
def category_page(request, slug):
    if slug == 'no_category':
        category = '미분류'
        post_list = Post.objects.filter(category=None)
    else:
        category = Category.objects.get(slug=slug)
        post_list = Post.objects.filter(category=category)
        return render(
            request,
            'blog/post_list.html',
            {
                'post_list': post_list,
                'categories': Category.objects.all(),
                'no_category_post_count': Post.objects.filter(category=None).count(),
                'category': category
            }
        )