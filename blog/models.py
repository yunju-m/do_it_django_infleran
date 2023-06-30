from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()            
    
    head_image = models.ImageField(upload_to='blog/images/%Y/%m/%d/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)    # 작성 시간(새로 만들어질 때 자동으로 업데이트)
    updated_at = models.DateTimeField(auto_now=True)        # 이미 존재하는 시간에 대해 변경내용 적용
    # author: 추후 작성 예정                

    ## django admin의 게시물 이름 설정
    def __str__(self):
        return f'[{self.pk}] {self.title}'
    
    def get_absolute_url(self):
        return f'/blog/{self.pk}/'