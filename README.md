# do_it_django_infleran

Do It 장고 + 부트스트랩

<div align="center">
<img width="329" alt="doitdj" src="/images/doitdj.png">

[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Fyunju-m&count_bg=%23FFBADA&title_bg=%23555555&icon=&icon_color=%23FFA8CC&title=hits&edge_flat=false)](https://hits.seeyoufarm.com)

</div>

# Do It Django Infleran 강의

> **강의 사이트 : [https://www.inflearn.com/course/%EB%91%90%EC%9E%87-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%9B%B9%EA%B0%9C%EB%B0%9C] ** <br/> **개발기간: 2023.06.21 ~ 2022.06.~ **

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

```
$ python -m venv venv
$ venv\Scripts\activate.bat
```

#### 가상환경 종료

```
$ deactivate
```

### django 개발환경

```
$ pip install django
$ pip list
$ django-admin startproject do_it_django_prj
$ python manage.py runserver
$ python manage.py migrate
$ python manage.py startapp blog
$ python manage.py startapp single_pages
```

### 새로운 앱 프로젝트 setting

```
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
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

### django super사용자 생성

```
$ python manage.py createsuperuser
$ username (leave blank to use 'saint'): yunju
$ Email address: yunju@doitdjango.com
$ Password:
$ Password (again):
Supperuser created successfully

$ python manage.py runserver
```

**127.0.0.1:8000/admin/** 접속 후 생성한 username, password을 입력하면 관리자 페이지 접속 가능

### model 변경 시 migrate 작업 필요

1. django에게 변경사항을 알려주는 작업

```
$ python manage.py makemigrations
```

2. 변경사항을 데이터베이스에 적용

```
$ python manage.py migrate
```

### 데이터베이스(db.sqlite) 확인 방법

#### admin 데이터베이스 확인

admin.py에서 생성한 Post모델을 불러오고 등록하면 127.0.0.1:8000/admin에 접속했을 때 Post 모델이 나오는 것을 확인할 수 있고 등록했던 title, content을 작성할 수 있다.

```
$ from .models import Post
$ admin.site.register(Post)
```

#### shell 데이터베이스 확인

```
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
