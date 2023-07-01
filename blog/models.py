from django.db import models
from django.contrib.auth.models import User
import os

class Post(models.Model):
    title = models.CharField(max_length=50)
    hook_text = models.CharField(max_length=100, blank=True)
    content = models.TextField()            
    
    head_image = models.ImageField(upload_to='blog/images/%Y/%m/%d/', blank=True)
    file_upload = models.FileField(upload_to='blog/files/%Y/%m/%d/', blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)  
    updated_at = models.DateTimeField(auto_now=True)        
    
    author = models.ForeignKey(User, on_delete=models.CASCADE)        

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