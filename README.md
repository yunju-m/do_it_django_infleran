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
```shell
$ pip install beautifulsoup4
```

### django-crispy-forms 설치
- 해당 실행환경 설정을 수행한 후 폼(form)을 꾸며본다.
- 줄간격, 크기 맞게 조절해주는 기능
[**외부 라이브러리를 이용한 django페이지 꾸미기**](#폼form-모양-예쁘게-개선하기)
1. django-crispy-forms 설치
- 사이트 : https://django-crispy-forms.readthedocs.io/en/latest/index.html
- 현재 bootstrap4을 이용하고 있으므로 crispy_bootstrap4 설치도 필요하다!!
```shell
$ pip install django-crispy-forms
$ python.exe -m pip install --upgrade pip
$ pip install crispy-bootstrap4
```

2. [settings.py에 "crispy_forms" 추가](#새로운-앱-프로젝트-setting)

3. settings.py에 템플릿 패키지 기본 값 설정
```python
INSTALLED_APPS = (
    ...
    'crispy_forms', 
    'crispy_bootstrap4',
)
```
- 이 프로젝트는 부트스트랩을 사용한다.
```python
CRISPY_TEMPLATE_PACK = 'bootstrap4'
``` 
만약 crispy-forms을 사용하려면 변경해주면된다.
```python
CRISPY_TEMPLATE_PACK = 'uni_form'
```

### django markdownx 마크다운 설치하기
1. django 마크다운을 설치한다.
사이트: https://neutronx.github.io/django-markdownx/
```shell
$ python -m pip install django-markdownx
$ git clone https://github.com/adi-/django-markdownx.git
$ cd django-markdownx/
$ python3 setup.py install
```

2. settings.py에 markdownx를 추가해준다.
```shell
INSTALLED_APPS = (
    'markdownx',
)
```

3. do_it_django앱의 urls.py에 다음 path를 추가해준다.
```shell
urlpatterns = [
    path('markdownx/', include('markdownx.urls')),
]
```
### django-allauth 설치
사이트 : https://django-allauth.readthedocs.io/en/latest/

1. django-allauth를 설치한다.
```shell
$ pip install django-allauth
```

2. INSTALLED_APPS에서 기본 추가해야할 코드와 구글로 로그인할 경우에 필요한 코드를 추가해준다.
(여러 종류가 있으므로 때에 따라 필요한 것을 추가)
```shell
INSTALLED_APPS = (
    'django.contrib.sites',

    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',   
)
```

- AUTHENTICATIONS_BACKENDS에 없으면 다음 코드를 추가해준다.
```shell
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',

    'allauth.account.auth_backends.AuthenticationBackend',
]
```

- TEMPLATES에 해당 코드가 없으면 추가해준다.
```shell
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
            ],
        },
    },
]
```

-  SITE_ID 지정 코드를 추가해준다.
- 가입할 때 이메일 주소를 받을 것인지 결정한다.
- 가입할 때 본인 확인하는 주소는 없이 가입가능하게한다.
```shell
SITE_ID = 1
ACCOUNT_EMAIL_REQUIRED = True
ACOOUNT_EMAIL_VERIFICATION = 'none'
```

3. do_it_django앱의 urls.py에 path를 지정해준다.
```python
urlpatterns = [
    ...
    path('accounts/', include('allauth.urls')),
    ...
]
```

4. 계정과 관련된 정보를 추가하기위해 migrate작업을 수행해준다.
```shell
$ python manage.py migrate
```

### django shell 성능 향상 기능
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
    "crispy_forms",
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
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=Docker&logoColor=white)

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