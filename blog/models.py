from django.db import models
from django.contrib.auth.models import User
import os
from markdownx.models import MarkdownxField
from markdownx.utils import markdown
from datetime import timedelta

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return f'/blog/category/{self.slug}/'
    
    class Meta:
        verbose_name_plural = 'Categories'

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True, allow_unicode=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return f'/blog/tag/{self.slug}/'

class Post(models.Model):
    title = models.CharField(max_length=50)
    hook_text = models.CharField(max_length=100, blank=True)
    content = MarkdownxField()           
    
    head_image = models.ImageField(upload_to='blog/images/%Y/%m/%d/', blank=True)
    file_upload = models.FileField(upload_to='blog/files/%Y/%m/%d/', blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)  
    updated_at = models.DateTimeField(auto_now=True)        
    
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)       
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
    tags = models.ManyToManyField(Tag, blank=True)

    ## django admin의 게시물 이름 설정
    def __str__(self):
        return f'[{self.pk}] {self.title} :: {self.author}'
    
    # 상세페이지 url
    def get_absolute_url(self):
        return f'/blog/{self.pk}/'
    
    # 파일이름 가져오는 함수
    def get_file_name(self):
        return os.path.basename(self.file_upload.name)
    
    # 확장자명을 가져오는 함수
    def get_file_ext(self):
        return self.get_file_name().split('.')[-1]
    
    # markdown 적용된 content 출력하는 함수
    def get_content_markdown(self):
        return markdown(self.content)
    
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)  
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.author}::{self.content}'
    
    def get_absolute_url(self):
        return f'{self.post.get_absolute_url()}#comment-{self.pk}'
    
    def is_updated(self):
        return self.updated_at - self.created_at > timedelta(seconds=1)