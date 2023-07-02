# do_it_django_infleran

Do It 장고 + 부트스트랩

<div align="center">
<img width="329" alt="doitdj" src="/blog/static/blog/images/doitdj.png">

[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Fyunju-m&count_bg=%23FFBADA&title_bg=%23555555&icon=&icon_color=%23FFA8CC&title=hits&edge_flat=false)](https://hits.seeyoufarm.com)

</div>

# Do It Django Infleran 강의

>**[강의 사이트](https://www.inflearn.com/course/%EB%91%90%EC%9E%87-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%9B%B9%EA%B0%9C%EB%B0%9C)** : Do It 장고 + 부트스트랩: 파이썬 웹 개발 <br>
**개발기간: 2023.06.21 ~ 2022.06.~**

## 프로젝트 소개

이 강의는 웹 개발을 하고 싶은 파이썬 사용자를 위한 강좌입니다. 실제 파이썬 진영의 가장 대표적인 웹 프레임워크 중 하나인 django를 이용해 여러분만의 블로그 사이트를 만들어 볼 수 있으며, 이 강의를 끝까지 따라하고 나면 여러분 모두 doitdjango.com 과 같은 웹사이트를 가질 수 있습니다.

이 강의에서는 HTML, CSS, 자바스크립트부터 부트스트랩, 파이썬 웹프레임워크인 장고(django), 도커(Docker), 아마존 웹서비스(AWS)까지 익힐 수 있습니다. 필요한 기능을 하나씩 구현하며 맞닥뜨리는 어려움을 직접 풀며 웹 개발에 대한 전반적인 이해와 함께 문제를 해결하는 능력까지 쌓아 보세요. 지금 바로 시작합시다!

## 시작 가이드

### Requirements

For building and running the application you need:

- [python 3.9.13](https://www.python.org/downloads/)
- [Django 4.2.2](https://docs.djangoproject.com/ko/4.2/intro/install/)
- [cmder 1.3.21](https://cmder.app/)
- [Pycharm](https://www.jetbrains.com/ko-kr/pycharm/download/#section=windows)
- [VisualStudioCode](https://code.visualstudio.com/download)

### git connection

```bash
$ git clone https://github.com/yunju-m/do_it_django_infleran.git
$ cd .
```

### venv 가상환경

#### 가상환경 설치 및 시작

```bash
$ python -m venv venv
$ venv\Scripts\activate.bat
```

#### 가상환경 종료

```bash
$ deactivate
```

### django 개발환경

```bash
$ pip install django
$ pip list
$ django-admin startproject do_it_django_prj
$ python manage.py runserver
$ python manage.py migrate
$ python manage.py startapp blog
$ python manage.py startapp single_pages
```

### Beautifulsoup4 설치
[**Beautifulsoup 이용한 TDD**](#tdd-테스트-주도-개발)
```shell
$ pip install beautifulsoup4
```

### django shell 성능 향상 기능
[**django shell_plus 이용한 다대일구조 확인**](#django-shell로-다대일구조-연결-확인)
```shell
$ pip install django_extensions
$ pip install ipython
```

### 새로운 앱 프로젝트 setting
- 앞서 설치한 django_extensions을 설정한다.

```python
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    
    "django_extensions",
    "blog",
    "single_pages",
]
```
---

## Stacks 🐈

### Environment

![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-007ACC?style=for-the-badge&logo=Visual%20Studio%20Code&logoColor=white)
![Pycharm](https://img.shields.io/badge/Pycharm-000000?style=for-the-badge&logo=Pycharm&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=Git&logoColor=white)
![Github](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=GitHub&logoColor=white)

### Development

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=Python&logoColor=white)
![Html](https://img.shields.io/badge/Html-E34F26?style=for-the-badge&logo=Html5&logoColor=white)
![Css](https://img.shields.io/badge/Css-1572B6?style=for-the-badge&logo=Css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=Javascript&logoColor=white)
![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=Django&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-7952B3?style=for-the-badge&logo=Bootstrap&logoColor=white)

---

## django project 기능 구현

### django super사용자 생성

```bash
$ python manage.py createsuperuser
$ username (leave blank to use 'saint'): yunju
$ Email address: yunju@doitdjango.com
$ Password:
$ Password (again):
Supperuser created successfully

$ python manage.py runserver
```

**127.0.0.1:8000/admin/** 접속 후 생성한 username, password을 입력하면 관리자 페이지 접속 가능

### model 변경 시 makemigrations, migrate

1. django에게 변경사항을 알려주는 작업

```bash
$ python manage.py makemigrations
```

2. 변경사항을 데이터베이스에 적용

```bash
$ python manage.py migrate
```

### 데이터베이스(db.sqlite) 확인 방법

#### admin 데이터베이스 확인

admin.py에서 생성한 Post모델을 불러오고 등록하면 127.0.0.1:8000/admin에 접속했을 때 Post 모델이 나오는 것을 확인할 수 있고 등록했던 title, content을 작성할 수 있다.

```python
$ from .models import Post
$ admin.site.register(Post)
```

#### shell 데이터베이스 확인

```bash
$ from blog.models import Post
$ Post.objects.all()
<QuerySet [<Post: [1] 첫번째 포스트>, <Post: [2] 두번째 포스트>]>
$ Post.objects.first()
<Post: [1] 첫번째 포스트>
$ Post.objects.last()
<Post: [1] 첫번째 포스트>

$ p = Post.objects.last()
$ p
<Post: [2] 두번째 포스트>
$ p.created_at
datetime.datetime(2023, 6, 24, 16, 12, 47)
$ p.updated_at
datetime.datetime(2023, 6, 24, 16, 15, 29, 366883)
$ p.title
'두 번째 포스트'
$ p.content
'두번째 포스트를 만들어보고 문제점이 무엇인지 확인해보자'
$ exit()
```

### FBV(Function Based View), CBV(Class Based View)

#### 1-1. FBV로 블로그 포스트 목록 페이지 만들기

1. admin.py에 model의 post함수의 데이터를 사용할 수 있도록 경로를 지정합니다.

```python
from .models import Post

admin.site.register(Post)
```

2. blog의 model.py에 게시물의 항목을 저장하는 변수를 선언합니다.

- **제목**: title
- **내용**: content
- **작성자**: author
- **작성시간**(새로 만들어질 때 자동으로 업데이트): created_at
- **이미 존재하는 시간에 대한 변경내용 적용**: updated_at

**🕓 한국(서울) 기준으로 시간을 맞추려면?** </br>

<p>django 프로젝트 파일의 setting.py 다음 내용을 변경합니다.</p>
TIME_ZONE = "UTC" ➡ "Asia/Seoul" </br>
USE_TZ = True ➡ False

- <p>def__str__(self)</p>: django admin의 게시물 이름 지정

```python
class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # author: 추후 작성 예정

    ## django admin의 게시물 이름 설정
    def __str__(self):
        return f'[{self.pk}] {self.title}'
```

3. do_it_django_prj의 url.py에 blog경로를 지정합니다.

```python
urlpatterns = [
    path("blog/", include('blog.urls')),
    path("admin/", admin.site.urls),
]
```

4. localhost:8000/blog에 접속하면 views.py에서 실행할 함수 경로를 지정합니다.

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
]
```

5. views.py에서 실행시킬 함수(index)를 선언합니다.
   render안에는 기본 **request**가 존재하고 **index.html를 반환**하여 화면에 나타냅니다.
   'post'는 model.py의 post함수의 총 데이터를 의미합니다.
   **.order_by('-pk')**: 기본키(pk)에 대해 최근 업데이트한 순서대로 정렬

```python
from django.shortcuts import render
from .models import Post

def index(request):
    posts = Post.objects.all().order_by('-pk')

    return render(
        request,
        'blog/index.html',
        {
            'posts': posts,
        }
    )
```

6. index.html에서 post모델의 데이터를 출력합니다.

```html
{% for p in posts %}
<hr />
<h3>{{ p.title }}</h3>
<h4>{{ p.created_at }}</h4>
<p>{{ p.content}}</p>
{% endfor%}
```

</br>

#### 1-2. FBV로 블로그 포스트 상세 페이지 만들기

**localhost:8000/blog/1**처럼 blog뒤에 게시물 pk가 오면 해당 게시물의 내용을 불러오는 상세 게시물 리스트 페이지를 만드는 방법은 다음과 같습니다.

1. urls.py에 blog/pk값 인 경로가 오면 실행되는 함수(single_post_page)를 선언합니다.

```python
urlpatterns = [
    path('<int:pk>/', views.single_post_page),
    path('', views.index),
]
```

2. views.py에 single_post_page 함수를 생성합니다.

- pk(기본키)를 인수로 받아 해당 pk가 동일한 Post.object를 posts라고 선언합니다.
- single_page.html에 posts를 'post'라는 이름으로 전달합니다.

```python
def single_post_page(request, pk):
    posts = Post.objects.get(pk=pk)

    return render(
        request,
        'blog/single_page.html',
        {
            'post': posts,
        }
    )
```

3. singe_page.html에 원하는 post 내역을 출력합니다.

```html
<a href="/blog/">Blog</a>
    </nav>
    <h1>{{ post.title }}</h1>
    <h4>{{ post.created_at }}</h4>
    <p>{{ post.content }}</p>
```

4. index.html에 post의 전체 내용을 반복문을 통해 출력합니다.

- 해당 게시물을 클릭하면 해당 게시물의 상세 리스트 페이지로 이동하는 함수 get_absolute_url을 호출합니다.

```html
{% for p in posts %}
<hr />
<h3>{{ p.title }}</h3>
<h3><a href="{{ p.get_absolute_url }}">{{ p.title }}</a></h3>
<h4>{{ p.created_at }}</h4>
<p>{{ p.content}}</p>
{% endfor%}
```

5. models.py에 get_absolute_url 함수를 선언합니다.

```python
def get_absolute_url(self):
    return f'/blog/{self.pk}/'
```

<br/>

#### 2-1. CBV로 블로그 포스트 목록 페이지 만들기

1. urls.py의 views.index ➡ views.PostList.as_view()

- as_view()를 마지막에 적어주는 것은 약속.

```python
urlpatterns = [
    path('<int:pk>/', views.single_post_page),
    path('', views.PostList.as_view()),
]
```

2. djago에서 제공하는 목록 리스트 항목을 출력하는 ListView 사용합니다.

- **model = Post**라고 이전의 지정.
- 최근 순으로 정렬: **ordering = '-pk'**
- ListView는 기본 post_list로 데이터를 저장하므로 경로를 변경하기위해서는 **template_name**사용
  혹은 index.html ➡ post_list.html 변경

```python
from django.shortcuts import render
from django.views.generic import ListView
from .models import Post

class PostList(ListView):
    model = Post
    template_name = 'blog/index.html'
    ordering = '-pk'
```

3. post_list.html에 post_list값 모두 출력

```html
{% for p in post_list %}
<hr />
<h3><a href="{{ p.get_absolute_url }}">{{ p.title }}</a></h3>
<h4>{{ p.created_at }}</h4>
```

</br>

#### 2-2. CBV로 블로그 포스트 상세 페이지 만들기

1. urls.py의 views.single_post_page ➡ views.PostDetail.as_view()

```python
urlpatterns = [
    path('<int:pk>/', views.PostDetail.as_view()),
    path('', views.PostList.as_view()),
]
```

2. djago에서 제공하는 상세 리스트 항목을 출력하는 DetailView를 사용합니다.

- **model = Post**라고 이전의 지정.
- ListView는 기본 post_detail로 데이터를 저장하므로 경로를 변경하기위해서는 **template_name**사용
  혹은 single_page_post.html ➡ post_detail.html 변경

```python
class PostDetail(DetailView):
    model = Post
```

3. post_detail.html에 원하는 post 데이터 항목 출력

<br/>

### 미디어 파일 관리하기

#### 이미지 파일 업로드

1. django project의 setting.py에서 MEDIA_URL, MEDIA_ROOT를 지정

- **MEDIA_URL**: 미디어 파일 제공 url 지정
- **MEDIA_ROOT**: 미디어 파일 저장 경로

```python
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, '_media')
```

2. blog models.py의 Post함수에 이미지 파일 변수 선언

- **blank=True**: 이미지가 존재하지 않아도 게시물 생성 허용
- 한 폴더안에 수많은 파일이 존재하면 모두 검색하는데 시간이 오래걸리고 느려지므로 생성날짜가 포함된 경로로 지정

```python
head_image = models.ImageField(upload_to='blog/images/%Y/%m/%d/', blank=True)
```

3. django project의 setting.py에서 MEDIA_URL, MEDIA_ROOT의 경로를 지정해준다.

```python

from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

4. post_list.html에 이미지를 출력해준다.

- **alt**: 이미지가 나오지않는 경우 출력하는 문장

```html
<img class="card-img-top" src="{{ p.head_image.url}}" alt="{{p.title}}" />
```

5. post_detail.html에 이미지를 출력한다.

- img-fluid rounded : 이미지를 꽉 채워서 둥글게 나타낸다.

```html
<img
  class="img-fluid rounded"
  src="{{ post.head_image.url }}"
  alt="{{ post.title }}"
/>
```

#### 파일 업로드를 위한 FileField

1. blog models.py의 Post함수에 파일 업로드 변수 선언

```python
    file_upload = models.FileField(upload_to='blog/files/%Y/%m/%d/', blank=True)
```

2. makemigration, migrate 작업 수행

```shell
$ python manage.py makemigrations
$ python manage.py migrate
```

3. /admin에 들어가서 Post 모델에 file upload창이 추가된 것을 확인할 수 있다. <br/>
   여기에 testfile.txt를 업로드하면 media/blog에 새로운 폴더 files가 생성되고 그안에 업로드한 testfile.txt이 생성된 것을 확인할 수 있다.

<br/>

### template tags & 조건문

#### 1. 템플릿에 조건문 사용

##### (1) if문으로 이미지가 없는 경우 처리하기

1. post_list.html

```html
{% if p.head_image %}
<img class="card-img-top" src="{{ p.head_image.url}}" alt="{{p.title}}" />
{%else %}
<img
  class="card-img-top"
  src="https://picsum.photos/seed/{{p.id}}/600/200"
  alt="{{p.title}}"
/>
{% endif %}
```

- lorem ipsum 사이트 : 긴 글문 예시 사이트
  영문 버전 : https://www.lipsum.com/
  한글 버전 : http://guny.kr/stuff/klorem/
- [lorem picsum 사이트](https://picsum.photos/) : 랜덤 이미지 제공 사이트
<p>picsum.photos를 갖는 이미지가 여러개인 경우 중복된 이미지가 출력되는 문제 발생❗❗</p>
<p>id값 or seed를 지정하여 이미지 구분 (id는 충돌 가능성 있으므로 seed추천)</p>

2. post_detail.html

```html
{% if post.head_image %}
<img
  class="img-fluid rounded"
  src="{{ post.head_image.url }}"
  alt="{{ post.title }}"
/>
{% else %}
<img
  class="card-img-top"
  src="https://picsum.photos/seed/{{p.id}}/600/200"
  alt="{{post.title}}"
/>
{%endif%}
```

##### (2) 첨부파일 다운로드 버튼 생성하기

1. post_detail.html

```html
<!--파일 다운로드 버튼 생성-->
{% if post.file_upload %}
<a
  href="{{ post.file_upload.url }}" type="button"
  class="btn btn-outline-dark"
  roll="button"
  download
  >Download</a
>
{%endif%}
```

##### (3) 첨부파일 종류별로 아이콘 나타내기

1. blog models.py에서 확장자를 알기 위해 파일 이름을 가져오는 함수를 생성한다.

```python
import os
def get_file_name(self):
    return os.path.basename(self.file_upload.name)
```

[Fontawesome](https://fontawesome.com/icons): 무료 아이콘 다운로드 사이트
- 사용하려면 head에 script 추가
```html
<script src="https://kit.fontawesome.com/c85c5556f3.js"></script>
```

2. 확장자 명을 가져오는 함수를 생성한다.

```python
def get_file_ext(self):
    return self.get_file_name().split('.')[-1]
```

3. post_detail.html 확장자 종류에 따라 아이콘 나타내기
```html
{% if post.file_upload %}
    <a href="{{ post.file_upload.url }}" type="button" class="btn btn-outline-dark" roll="button" download="download">Download:
    {% if post.get_file_ext == 'xlsx' or post.get_file_ext == 'xls' %}
        <i class="fa-regular fa-file-excel"></i>
    {% elif post.get_file_ext == 'csv' %}
        <i class="fa-regular fa-file-csv"></i>
    {% elif post.get_file_ext == 'docx'%}
        <i class="fa-regular fa-file-word"></i>
    {% else %}
        <i class="fa-regular fa-file"></i>
    {%endif%}
    {{ post.get_file_name }}</a>
{%endif%}
```
<br>

#### 2. template tags 사용하여 미리보기 생성
**truncatechars & truncatewords**
1. post_list.html truncatewords 추가
- 지정크기만큼 글자수 출력
```html
<p class="card-text">{{p.content | truncatewords:45}}</p>
```
<span style="color:red">
truncatedword: 45와 같이 띄어쓰기x
</span>

<br>

#### 3. 요약문 추가하기
1. blog models.py에 요약문 변수를 생성한다.
```python
hook_text = models.CharField(max_length=100, blank=True)
```

2. makemigraions, migrate 수행한다.
```shell
$ python.manage.py makemigrations
$ python manage.py migrate
```

3. /admin에 들어가면 hook_text가 새로 생성 된 것을 확인할 수 있다.

4. post_list.html, post_detail.html에 hook_text가 있을 때 출력
- **text-muted**: 흐리게 글씨 표현
- post_list: p.hook_text /  post_detail: post.hook_text
```html
{% if p.hook_text %}
    <h5 class="text-muted">{{p.hook_text}}</h5>
{%endif%}
``` 
<br>

### TDD 테스트 주도 개발
#### TDD (Test Driven Development)란?
1. 구성
테스트 코드 작성 ➡ 기능 구현 ➡ 리팩토링

2. Beautifulsoup4 설치
- 브라우저에 구현한 내용이 제대로 표현되었는지 확인하기 위한 라이브러리
- 웹 크롤링 할 때 사용
```shell
$ pip install beautifulsoup4
```

<br>

#### 테스트 코드 만들기
##### 1. 블로그 목록 페이지에 대한 테스트 코드
blog 앱 폴더의 tests.py에서 테스트 케이스 생성
1-1. 포스트 목록 페이지(post list)을 연다.
- Client() : 웹 사이트 방문자의 브라우저

```python
class TestView(TestCase):
    def setUp(self):
        self.client = Client()

response = self.client.get('/blog/')
```
1-2. 정상적으로 페이지가 로드된다.
```python
self.assertEqual(response.status_code, 200)
```
1-3. 페이지의 타이틀에 Blog라는 문구가 있다.
```python
soup = BeautifulSoup(response.content, 'html.parser')
self.assertIn('Blog',soup.title.text)
```
1-4. 상단에 NavBar가 있다.
```python
navbar = soup.nav
```
1-5. Blog, About me라는 문구가 Navbar에 있다.
```python
self.assertIn('Blog', navbar.text)
self.assertIn('Blog', navbar.text)
```
<br>
2-1. 게시물이 하나도 없을 때

```python
self.assertIn(Post.objects.count(), 0)
```
2-2. 메인 영역에 "아직 게시물이 없습니다."라는 문구가 나온다.
```python
main_area = soup.find('div', id='main-area')
self.assertIn('아직 게시물이 없습니다.', main_area.text)
```

<br>

3-1. 만약 게시물이 2개 있다면
```python
post_001 = Post.objects.create(
    title = "첫 번째 포스트 입니다.",
    content = "Hello World! We are the World",
)
        
post_002 = Post.objects.create(
    title = "두 번째 포스트 입니다.",
    content = "저는 마라탕과 떡볶이를 사랑합니다",
)
```
3-2. 포스트 목록 페이지를 새로 고침 했을 때
```python
self.assertEqual(Post.objects.count(), 2)
response =self.client.get('/blog/')
```
3-3. 메인 영역에 포스트 2개의 타이틀이 존재한다.
```python
soup = BeautifulSoup(response.content, 'html.parser')
main_area = soup.find('div', id='main-area')
self.assertIn(post_001.title, main_area.text)
self.assertIn(post_002.title, main_area.text)
```
3-4, "아직 게시물이 없습니다"라는 문구가 없어진다.

<br>

##### 2. 블로그 상세 페이지에 대한 테스트 코드
1-1. 포스트가 하나 있다.
```python
post_001 = Post.objects.create(
    title = "첫 번째 포스트 입니다.",
    content = "Hello World! We are the World",
)
self.assertEqual(Post.objects.count(), 1)
```
1-2. 그 포스트의 url은 '/blog/1/'이다.
```python
self.assertEqual(post_001.get_absolute_url(), '/blog/1/')
```
2-1. 그 포스트의 url로 접근하면 정상적으로 작동한다.(status_code: 200)
```python
response = self.client.get(post_001.get_absolute_url())
self.assertEqual(response.status_code, 200)
```
2-2. 포스트 목록 페이지와 똑같은 내비게이션 바가 있다.
```python
soup = BeautifulSoup(response.content, 'html.parser')
navbar = soup.nav
self.assertIn('Blog', navbar.text)
self.assertIn('About me', navbar.text)
```
2-3. 첫 번째 포스트의 목록이 웹 브라우저 웹 타이틀에 들어있다.
```python
self.assertIn(post_001.title, soup.title)
```
2-4. 첫 번째 포스트의 제목이 포스트 영역에 있다.
```python
main_area = soup.find('div', id='main-area')
post_area = main_area.find('div', id='post-area')
self.assertIn(post_001.title, post_area.text)
```
2-5. 첫 번째 포스트의 작성자(author)가 포스트 영역에 있다. <br>
[포스트 상세 페이지 작성자 추가하기](#포스트-상세-페이지-작성자author) 

2-6. 첫 번쩨 포스트의 내용(content)가 포스트 영역에 있다.
```python
self.assertIn(post_001.content, post_area.text)
```

<br>

### 템플릿 파일 모듈화 하기
#### 1. extends - 화면 메인 영역 모듈화하기
1. base.html 생성
- post_list.html와 post_detail.html을 모듈화하는 html
- post_list.html 복사

2. post_list.html 
- base.html에 main-area부분에 넣기위해 상단에 다음과 같은 코드를 추가한다.
```html
{% extends 'blog/base.html' %}
```
- base.html의 main-area에 넣을 코드를 block사이에 넣어준다.
```html
{% block main_area %}
{% endblock %}
```

3. post_detail.html
- base.html에 main-area부분에 넣기위해 상단에 다음과 같은 코드를 추가한다.
```html
{% extends 'blog/base.html' %}
```
- 해당 게시물을 클릭하면 게시물 제목으로 변경되도록 한다.
```html
{% block head_title %}
  {{ post.title }}
  | Blog
{% endblock %}
```
- base.html의 main-area에 넣을 코드를 block사이에 넣어준다.
```html
{% block main_area %}
{% endblock %}
```
<br>

#### 2. include - 네비게이션바, footer 모듈화하기
1. 중복 네비게이션바 테스트에 대해 navbar_test 함수 생성한다.
- **test_가 먼저 나오는 이름을 가진 함수로 시작하면 하나의 TestCase(유닛테스트)로 인식한다.**
```python
def navbar_test(self, soup):
    navbar = soup.nav
    self.assertIn('Blog', navbar.text)
    self.assertIn('Blog', navbar.text)
```
- 위의 내용에 있던 자리에는 함수를 호출해준다.
```python
self.navbar_test(soup)
```

2. 네비게이션바에 있는 Logo, Home, Blog, About me 하이퍼링크에 대해 경로 변경 테스트
- a 링크의 속성 중 href 경로에 대해 같은지 확인한다.

```python
def navbar_test(self, soup):
    navbar = soup.nav
    self.assertIn('Blog', navbar.text)
    self.assertIn('Blog', navbar.text)

    logo_btn = navbar.find('a', text='Do It Django')
    self.assertEqual(logo_btn.attrs['href'], '/')

    home_btn = navbar.find('a', text='Home')
    self.assertEqual(home_btn.attrs['href'], '/')

    blog_btn = navbar.find('a', text='Blog')
    self.assertEqual(blog_btn.attrs['href'], '/blog/')

    about_me_btn = navbar.find('a', text='About me')
    self.assertEqual(about_me_btn.attrs['href'], '/about_me/')
```
3. navbar.html을 생성하고 base.html에 있는 네비게시션바, 모달 파트를 넣어준 후 그 위치에 다음 코드를 넣어준다.
```html
{% include 'blog/vavbar.html' %}
```

4. footer.html을 생성하고 base.html에 있는 footer 파트를 넣어준 후 그 위치에 다음 코드를 넣어준다.
```html
{% include 'blog/footer.html' %}
```
<br>

### 다대일 관계
#### 작성자(author) 생성하기
1. blog 앱의 models.py에 author 추가하기
- **CASCADE**: user가 탈퇴하면 해당 user의 게시글도 삭제(외래키참조 삭제)
- **SET_NULL**: user가 탈퇴해도 해당 user의 게시글은 유지된다.
이때, **null=True**로 지정해줘야 한다.
```python
from django.contrib.auth.models import User

1. CASCADE인 경우
author = models.ForeignKey(User, on_delete=models.CASCADE)

2. SET_NULL인 경우
author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)  
```

2. /admin/에서 user에서 새로운 사용자를 생성한 후 해당 post에 대해 author 지정이 가능하다. 
- CASCADE인 경우: user를 삭제하면 해당 post글도 자동으로 삭제되는 것을 확인할 수 있다.
- SET_NULL인 경우: uesr를 삭제해도 해당 post글은 유지되는 것을 알 수 있다. (해당 글에 대해서 author는 **None**이 된다.)

#### 포스트 목록, 포스트 상세 페이지에 작성자 정보 출력하기
- blog앱의 tests.py의 setUp 함수에 user계정을 생성한다.
- test를 실행할 때 초반에 user가 2명있다고 인식하게된다.
```python
self.user_trump = User.objects.create_user(
    username='yunju',
    password='0129',
)
self.user_trump = User.objects.create_user(
    username='subin',
    password='0313',
)
```
##### 포스트 목록 페이지 작성자(author)
1. test_post_list 함수의 각 post_001, post_002에 author을 지정해준다.
```python
post_001 = Post.objects.create(
    title = "첫 번째 포스트 입니다.",
    content = "Hello World! We are the World",
    author=self.user_yunju
)
        
post_002 = Post.objects.create(
    title = "두 번째 포스트 입니다.",
    content = "저는 마라탕과 떡볶이를 사랑합니다",
    author=self.user_subin
)
```

2. 게시글에 작성자 명을 추가해주기 위해 test_post_list에 다음 코드를 추가한다.
```python
self.assertIn(post_001.author.username.upper(), main_area.text)
self.assertIn(post_002.author.username.upper(), main_area.text)
```

3. post_list.html에 개발자명에 해당 부분을 다음으로 수정한다.
- upper: 대문자로 표현
```html
<a href="#">{{ p.author | upper }}</a>
```

##### 포스트 상세 페이지 작성자(author)
1. test_post_detail 함수의 post_001에 author를 추가한다.
```python
post_001 = Post.objects.create(
    title = "첫 번째 포스트 입니다.",
    content = "Hello World! We are the World",
    author = self.user_yunju
)
```

2. 첫 번째 포스트의 작성자(author)가 포스트 영역에 표시한다.
```python
self.assertIn(self.user_yunju.username.upper(), post_area.text)
```

3.  post_detail.html에 개발자명에 해당 부분을 다음으로 수정한다.
```html
<!-- Author -->
<p class="lead">
by
<a href="#">{{ post.author | upper }}</a>
</p>
```
<br>

#### Category 생성하기
1. blog앱의 models.py에 Category class를 생성한다.
- name: 카테고리 이름, 중복x
- slug: 카테고리 클릭 시 url 뒤에 카테고리 이름이 붙어서 읽을 수 있게 한다.
ex, food 카테고리를 클릭한 경우
localhost:8000/blog/food/
    - allow_unicode: 한글 지원
    - self.name을 반환받는 함수 지정
```python
class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)

    def __str__(self):
        return self.name
```

2. Post 모델에 카테고리 추가한다.
```python
category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
```

3. makemigrations, migrate 작업 수행한다.
```shell
$ python manage.py makemigrations
$ python manage.py migrate
```
4. admins.py에 Category를 추가해준다.
- Category의 name을 입력하면 자동으로 slug에도 입력되도록 설정한다.
```python
from .models import Category

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Category, CategoryAdmin)

```

5. /admin의 Category 이름을 변경하기 위해 models.py에 다음을 추가해준다.
```python
class Meta:
    verbose_name_plural = 'Categories'
```

| blank=True | null=True |
| :--------: | :-------: |
| 사용자가 form을 입력할 때 필수사항이 모두 포함되어 있는지 판단 <br> 삭제되거나 수정, 탈퇴에 영향x | 데이터베이스의 필수사항을 결정 <br> 삭제, 수정에 영향o, 운영방침을 정한다. | 

<br>

#### django shell로 다대일구조 연결 확인
1. 기본 shell을 이용한 모델(Post, Category) 확인
```shell
$ python manage.py shell
>>> from blog.models import Post, Category
>>> Post.objects.count()
5
>>> Category.objects.count()
3
>>> for p in Post.objects.all():
...     print(p)
...
[1] 첫번째 포스트 :: yunju
[2] 두번째 포스트 :: yunju
[3] 세번째 포스트 :: yunju
[5] Django 인프런 강의 수강 :: yunju
[6] Django는 파이썬 프레임워크 :: yunju
>>> for c in Category.objects.all():
...     print(c)
...
programming
django
cat
```

2. django_extension 라이브러리를 이용한 shell_plus 이용
```shell
In [1]: for p in Post.objects.all():
...:        print(p)
...:
[1] 첫번째 포스트 :: yunju
[2] 두번째 포스트 :: yunju
[3] 세번째 포스트 :: yunju
[5] Django 인프런 강의 수강 :: yunju
[6] Django는 파이썬 프레임워크 :: yunju

In [2]: for c in Category.objects.all():
   ...:     print(c)
   ...:
programming
django
cat

In [5]: category_programming = Category.objects.get(slug="django")

In [6]: category_proogramming
Out[6]: <Category: django>

## 카테고리 필드명은 .대신 __를 사용하여 정보를 얻어올 수 있다.
In [7]: category_proogramming = Category.objects.get(name__startswith="cat")

In [8]: category_proogramming
Out[8]: <Category: cat>

In [9]: for p in category_programming.post_set.all():
    ...:     print(p)
    ...:
[5] Django 인프런 강의 수강 :: yunju
[6] Django는 파이썬 프레임워크 :: yunju

In [10] exit()
```
<br>

#### 포스트 목록 페이지 수정하기
##### 1. 카테고리에 대한 테스트 코드 작성
1-1. blog앱의 tests.py에 setUp함수에 카테고리를 생성한다.
```python
from .models import Category

self.category_programming = Category.objects.create(
    name='programming', slug='programming'
)
self.category_music = Category.objects.create(
    name='music', slug='music'
)
```

1-2. blog앱의 tests.py에 setUp함수에 포스트 3개를 생성한다.
```python
self.post_001 = Post.objects.create(
    title = "첫 번째 포스트 입니다.",
    content = "Hello World! We are the World",
    author=self.user_yunju,
    category=self.category_programming
)
self.post_002 = Post.objects.create(
    title = "두 번째 포스트 입니다.",
    content = "저는 마라탕과 떡볶이를 사랑합니다",
    author=self.user_subin,
    category=self.category_music
)
self.post_003 = Post.objects.create(
    title = "세 번째 포스트 입니다.",
    content = "Category가 없는 포스트입니다.",
    author=self.user_yunju
)
```

2. test_post_list를 포스트가 있는 경우와 없는 경우로 구분해준다.
- test_post_list_with_post
```python
# 포스트가 있는 경우
def test_post_list_with_posts(self):
    self.assertEqual(Post.objects.count(), 3)

    response = self.client.get('/blog/')
    self.assertEqual(response.status_code, 200)

    soup = BeautifulSoup(response.content, 'html.parser')
    self.assertIn('Blog', soup.title.text)

    self.navbar_test(soup)      

    main_area = soup.find('div', id='main-area')

    self.assertIn(self.post_001.author.username.upper(), main_area.text)
    self.assertIn(self.post_002.author.username.upper(), main_area.text)
```
- test_post_list_without_post
```python
# 포스트가 없는 경우
def test_post_list_without_posts(self):
    Post.objects.all().delete()
    self.assertEqual(Post.objects.count(), 0)

    response = self.client.get('/blog/')
    self.assertEqual(response.status_code, 200)

    soup = BeautifulSoup(response.content, 'html.parser')
    self.navbar_test(soup)
    self.assertIn('Blog', soup.title.text)
    
    main_area = soup.find('div', id='main-area')
    self.assertIn('아직 게시물이 없습니다.', main_area.text)
```

##### 2. 포스트(카드)안에 카테고리 문구 생성
1. 포스트 있는 경우(test_post_list_with_posts) 각 포스트에 해당하는 카드를 생성
- main-area안에 카드 존재
```python
post_001_card = main_area('div', id='post-1')
    self.assertIn(self.post_001.title, post_001_card.text)
    self.assertIn(self.post_001.category.name, post_001_card.text)

    post_002_card = main_area('div', id='post-2')
    self.assertIn(self.post_002.title, post_002_card.text)
    self.assertIn(self.post_002.category.name, post_002_card.text)

    post_003_card = main_area('div', id='post-3')
    self.assertIn(self.post_003.title, post_003_card.text)
    self.assertIn('미분류', post_003_card.text)
```

2. 카테고리 카드 안에 카테고리 문구 추가
```python
def category_card_test(self, soup):
    categories_card = soup.find('div', id='categories-card')
    self.assertIn('Categories', categories_card.text)
    self.assertIn(
        f'{self.category_programming}({self.category_programming.post_set.count()})',
        categories_card.text
    )
    self.assertIn(
        f'{self.category_music}({self.category_music.post_set.count()})',
        categories_card.text
    )
    self.assertIn(
        f'미분류({Post.objects.filter(caegory=None).count()})',
        categories_card.text
    )
```

3. test_post_list_with_posts 함수에 카테고리 카드 테스트 함수를 호출해준다.
```python
self.category_card_test(soup)
```
 
4. views.py의 PostList 함수에 카테고리를 포함하는 context를 반환하는 함수를 생성해준다.
```python
from .models import Post, Category

def get_context_data(self, **kwargs):
    context = super(PostList, self).get_context_data()
    context['categories'] = Category.objects.all()
    context['no_category_post_count'] = Post.objects.filter(category=None).count()
    return context
```

5. base.html의 카테고리 부분을 categories가 출력되도록 변경해준다.
- id : categories-card
- categories에 있는 각 category에 대해 이름과 개수를 출력한다.
```html
<a href="#">{{ category.name }} ({{ category.post_set.count }})</a>
<a href="#">{{ category.name }} 
            ({{ category.post_set.count }})</a>
```
- 다음과 같은 경우에는 오류가 발생한다.
<span style="color:red">
category_card_test 함수에서처럼 띄어쓰기까지 동일하게 이름과 개수를 출력하도록 설정해야한다.
</span>

```html
<!-- Categories widget-->
<div class="card mb-4" id="categories-card">
<div class="card-header">Categories</div>
<div class="card-body">
    <div class="row">
    <ul>
        {% for category in categories %}
        <li>
            <a href="#">{{ category.name }}({{ category.post_set.count }})</a>
        </li>
        {% endfor %}
        <li>
        <a href="#">미분류({{ no_category_post_count }})</a>
        </li>
    </ul>
    </div>
</div>
```

6. post_list.html에 카테고리 별 id와 배지를 등록해준다.
- 카테고리 카드의 id는 post별로 id 값을 지닌다.
```html
<div class="card mb-4" id="post-{{ p.id }}">
```
- 카테고리가 존재하면 해당 카테고리 이름을 가진 배지를 생성한다.
- 카테고리가 없으면 미분류 배지를 생성한다.
```html
{% if p.category %}
    <span class="badge badge-secondary float-right">{{ p.category }}</span>
{% else %}
    <span class="badge badge-secondary float-right">미분류</span>
{% endif%}
```

<br>

#### 포스트 상세 페이지 수정하기
1. blog앱 tests.py의 test_post_detail 함수에 category_card_test함수를 추가해준다.
```python
self.category_card_test(soup)
``` 

2. 포스트 제목 옆에 카테고리도 나타나도록 해준다.
```python
self.assertIn(self.post_001.category.name, post_area.text)
```

3. views.py에 PostDetail 함수에 PostList와 동일하게 get_context_data 함수를 생성하여 카테고리 데이터를 불러오도록 해준다.
```python
class PostDetail(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super(PostDetail, self).get_context_data()
        context['categories'] = Category.objects.all()
        context['no_category_post_count'] = Post.objects.filter(category=None).count()
        return context
```

4. post_list.html와 동일하게 post_detail.html에도 해당 카테고리별 배지를 출력하는 문장을 넣어준다.
```html
{% if post.category %}
    <span class="badge badge-secondary float-right">{{ post.category }}</span>
{% else %}
    <span class="badge badge-secondary float-right">미분류</span>
{% endif%}
```

<br>

#### 카테고리별 페이지 나타내기
1. blog앱 tests.py에 카테고리별 페이지가 나타나도록 하는 함수 test_category_page를 생성한다.
- category_programming에 대한 client를 response로 지정
- models.py에서 선언한 고유 url를 반환하는  get_absolute_url함수를 호출한다.
- 네비게이션 바, 카테고리가 제대로 작동하는지 테스트
- main-area div안과 h1에 category_programming이름을 넣어준다.
- main_area.text에는 post_001의 제목이 존재하는지 파악하고 post_002, post_003은 존재하지 않아야 한다.
```python
def test_category_page(self):
    response = self.client.get(self.category_programming.get_absolute_url())
    self.assertEqual(response.status_code, 200)

    soup = BeautifulSoup(response.content, 'html.parser')
    self.navbar_test(soup)
    self.category_card_test(soup)

    main_area = soup.find('div', id='main-area')
    self.assertIn(self.category_programming.name, main_area.h1.text)
    self.assertIn(self.category_programming.name, main_area.text)
    self.assertIn(self.post_001.title, main_area.text)
    self.assertNotIn(self.post_002.title, main_area.text)
    self.assertNotIn(self.post_003.title, main_area.text)
```

2. models.py의 Category모델에 고유 url을 갖도록 get_absolute_url 함수를 생성한다.
- slug는 고유한 값이다.
```python 
def get_absolute_url(self):
    return f'/blog/category/{self.slug}/'
```

3. 해당 경로에 대해 urls.py에 생성한다.
- 소문자인 경우 : **함수**
💓 category_page는 소문자이므로 함수이다.
- 대문자인 경우 : **클래스**
```python
urlpatterns = [
    path('category/<str:slug>/', views.category_page),
    path('<int:pk>/', views.PostDetail.as_view()),
    path('', views.PostList.as_view()),
]

```
4. views.py에 category_page 함수를 생성한다.
```python
def category_page(request, slug):
    category = Category.objects.get(slug=slug)
    return render(
        request,
        'blog/post_list.html',
        {
            'post_list': Post.objects.filter(category=category),
            'categories': Category.objects.all(),
            'no_category_post_count': Post.objects.filter(category=None).count(),
            'category': category
        }
    )
```

5. post_list.html에 category_page로부터 받은 category가 있다면 h1에 출력해준다.
```html
<h1>
Blog
{% if category %}
    <span class="badge badge-secondary float-right">{{ category }}</span>
{% endif %}
</h1>
```

6. base.html에 category에 대한 고유 url로 이동하도록 지정해준다.
```html
<!-- Categories widget-->
<div class="card mb-4" id="categories-card">
    <div class="card-header">Categories</div>
    <div class="card-body">
        <div class="row">
        <ul>
            {% for category in categories %}
            <li>
                <a href="{{ category.get_absolute_url }}">{{ category.name }}({{ category.post_set.count }})</a>
            </li>
            {% endfor %}
            <li>
            <a href="/blog/category/no_category/">미분류({{ no_category_post_count }})</a>
            </li>
        </ul>
        </div>
    </div>
</div>
```

7. category가 없는 경우 no_category url에 대한 views.py에 조건을 추가해준다.
```python
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
```
<br>

### 다대다 관계
#### Tag 모델 생성하기
1. blog앱 models.py에 Tag 모델을 생성한다.
```python
class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True, allow_unicode=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return f'/blog/tag/{self.slug}/'
```

2. Post 모델에 tag에 대한 변수를 생성한다.
- 다대다관계를 가지므로 ManyToManyField를 가진다.
```python
tags = models.ManyToManyField(Tag, blank=True)
```

3. makemigraions, migrate 수행

4. admin.py에 Tag에 대한 레지스터를 생성한다.
```python
from .models import  Tag

class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Tag, TagAdmin)
```

#### 포스트 목록 페이지에 tag 추가하기
1.  tests.py의 setUp 함수에 tag 3가지를 생성한다.
```python
# 태그 생성
self.tag_python_kar = Tag.objects.create(
    name="파이썬 공부", slug='파이썬-공부'
)
self.tag_python = Tag.objects.create(
    name="python", slug='python'
)
self.tag_django = Tag.objects.create(
    name="django", slug='django'
)
```
2. post_001과 post_003에 tag를 추가해준다.
```python
self.post_001.tas.add(self.tag_django)
self.post_003.tags.add(self.tag_django)
self.post_003.tags.add(self.tag_python)
```

3. test_post_list_with_posts 함수에 각 포스트에 대해 tag가 있는 포스트들은 tag를 assertIn 해주고 없는 tag들에 대해서는 assertNotIn을 해준다.
- post_001_card: django 태그
- post_003_card: python, django 태그
```python
# post_001_card
self.assertIn(self.tag_django.name, post_001_card.text)
self.assertNotIn(self.tag_python.name, post_001_card.text)
self.assertNotIn(self.tag_python_kar.name, post_001_card.text)

# post_002_card
self.assertNotIn(self.tag_django.name, post_002_card.text)
self.assertNotIn(self.tag_python.name, post_002_card.text)
self.assertNotIn(self.tag_python_kar.name, post_002_card.text)

# post_003_card
self.assertIn(self.tag_django.name, post_003_card.text)
self.assertIn(self.tag_python.name, post_003_card.text)
self.assertNotIn(self.tag_python_kar.name, post_003_card.text)        

```

4. /admin에 접속하여 tag을 생성한다.

5. post_list.html에 tag가 있으면 tag아이콘과 함께 추가한다.
- iterator를 사용하면 서버 부하 덜 부담준다.
```html
{% if p.tags.exists %}
<i class="fa-solid fa-tags"></i>
{% for tag in p.tags.iterator %}
<a href="{{ tag.get_absolute_url }}">
    <span class="badge badge-light">{{ tag }}</span></a>
{% endfor %}
<br/><br/>
{% endif %}
```
<br>

#### 포스트 상세 페이지에 tag 추가하기
1. blog앱 tests.py의 test_post_detail함수에도 동일하게 tag가 있는지 확인하는 코드를 추가해준다.
- 상세페이지의 tag는 카드안에 있는게 아니라 post_area안에 있으므로 변경해준다.

```python
self.assertIn(self.tag_django.name, post_area.text)
self.assertNotIn(self.tag_python.name, post_area.text)
self.assertNotIn(self.tag_python_kar.name, post_area.text)
```

2. post_detail.html에 post_list.html와 동일하게 tag가 있으면 출력하도록 해준다.
```html
<!--Tag Content-->
{% if post.tags.exists %}
    <i class="fa-solid fa-tags"></i>
    {% for tag in post.tags.iterator %}
    <a href="{{ tag.get_absolute_url }}">
        <span class="badge badge-light">{{ tag }}</span></a>
    {% endfor %}
    <br/><br/>
{% endif %}
```
<br>

#### tag 페이지 생성하기
- tag를 클릭했을 때 해당 tag의 페이지가 나타나도록 한다.
 
1. tests.py에 tag페이지가 나타나는 함수 test_tag_page를 생성한다.
```python
def test_tag_page(self):
    response = self.client.get(self.tag_django.get_absolute_url())
    self.assertEqual(response.status_code, 200)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    self.navbar_test(soup)
    self.category_card_test(soup)

    self.assertIn(self.tag_django.name, soup.h1.text)
    main_area = soup.find('div', id='main-area')
    self.assertIn(self.tag_django.name, main_area.text)

    self.assertIn(self.post_001.title, main_area.text)
    self.assertNotIn(self.post_002.title, main_area.text)
    self.assertIn(self.post_003.title, main_area.text)
```
2. urls.py에 tag의 경로를 지정해준다.
```python
urlpatterns = [
    path('tag/<str:slug>/', views.tag_page),
    path('category/<str:slug>/', views.category_page),
    path('<int:pk>/', views.PostDetail.as_view()),
    path('', views.PostList.as_view()),
]
```

3. views.py에 태그별 페이지를 반환하는 함수를 생성해준다.
- category_page 함수와 거의 유사하다.
```python
# 태그별 페이지 반환 함수
def tag_page(request, slug):
    tag = Tag.objects.get(slug=slug)
    post_list = tag.post_set.all()
    return render(
        request,
        'blog/post_list.html',
        {
            'post_list': post_list,
            'categories': Category.objects.all(),
            'no_category_post_count': Post.objects.filter(category=None).count(),
            'tag': tag
        }
    )
```

4. post_list.html의 h1에 tag가 있으면 tag을 출력해준다.
- 카테고리와 구분하기 위해 tag를 클릭하면 tag 아이콘과 함께 출력한다.
```html
<h1>
    Blog
    {% if category %}
      <span class="badge badge-secondary">{{ category }}</span>
    {% endif %}
    {% if tag %}
      <span class="badge badge-light">
        <i class="fa-solid fa-tags"></i>
        {{ tag }}
        ({{ tag.post_set.count }})</span>
    {% endif %}
</h1>
```