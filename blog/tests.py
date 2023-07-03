from django.test import TestCase, Client
from bs4 import BeautifulSoup
from .models import Post, Category, Tag
from django.contrib.auth.models import User

class TestView(TestCase):
    def setUp(self):
        self.client = Client()
        # 사용자 생성
        self.user_yunju = User.objects.create_user(
            username='yunju',
            password='0129'
        )
        self.user_subin = User.objects.create_user(
            username='subin',
            password='0313'
        )

        # 카테고리 생성
        self.category_programming = Category.objects.create(
            name='programming', slug='programming'
        )
        self.category_music = Category.objects.create(
            name='music', slug='music'
        )

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

        # 포스트 생성
        self.post_001 = Post.objects.create(
            title = "첫 번째 포스트 입니다.",
            content = "Hello World! We are the World",
            author=self.user_yunju,
            category=self.category_programming
        )
        self.post_001.tags.add(self.tag_django)

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
        self.post_003.tags.add(self.tag_django)
        self.post_003.tags.add(self.tag_python)
    
    # 내비게이션바 함수
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

    # 카테고리 카드 함수
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
            f'미분류({Post.objects.filter(category=None).count()})',
            categories_card.text
        )

    # 포스트가 있는 경우
    def test_post_list_with_posts(self):
        self.assertEqual(Post.objects.count(), 3)

        response = self.client.get('/blog/')
        self.assertEqual(response.status_code, 200)

        soup = BeautifulSoup(response.content, 'html.parser')
        self.assertIn('Blog', soup.title.text)

        self.navbar_test(soup)
        self.category_card_test(soup)

        main_area = soup.find('div', id='main-area')

        post_001_card = main_area.find('div', id='post-1')
        self.assertIn(self.post_001.title, post_001_card.text)
        self.assertIn(self.post_001.category.name, post_001_card.text)
        self.assertIn(self.tag_django.name, post_001_card.text)
        self.assertNotIn(self.tag_python.name, post_001_card.text)
        self.assertNotIn(self.tag_python_kar.name, post_001_card.text)

        post_002_card = main_area.find('div', id='post-2')
        self.assertIn(self.post_002.title, post_002_card.text)
        self.assertIn(self.post_002.category.name, post_002_card.text)
        self.assertNotIn(self.tag_django.name, post_002_card.text)
        self.assertNotIn(self.tag_python.name, post_002_card.text)
        self.assertNotIn(self.tag_python_kar.name, post_002_card.text)

        post_003_card = main_area.find('div', id='post-3')
        self.assertIn(self.post_003.title, post_003_card.text)
        self.assertIn('미분류', post_003_card.text)
        self.assertIn(self.tag_django.name, post_003_card.text)
        self.assertIn(self.tag_python.name, post_003_card.text)
        self.assertNotIn(self.tag_python_kar.name, post_003_card.text)

        self.assertIn(self.post_001.author.username.upper(), main_area.text)
        self.assertIn(self.post_002.author.username.upper(), main_area.text)

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

    # 상세페이지 함수
    def test_post_detail(self):
        self.assertEqual(Post.objects.count(), 3)

        self.assertEqual(self.post_001.get_absolute_url(), '/blog/1/')

        response = self.client.get(self.post_001.get_absolute_url())
        self.assertEqual(response.status_code, 200)

        soup = BeautifulSoup(response.content, 'html.parser')
        self.navbar_test(soup)
        self.category_card_test(soup)

        self.assertIn(self.post_001.title, soup.title.text)

        main_area = soup.find('div', id='main-area')
        post_area = main_area.find('div', id='post-area')
        
        self.assertIn(self.post_001.title, post_area.text)
        self.assertIn(self.post_001.category.name, post_area.text)

        self.assertIn(self.user_yunju.username.upper(), post_area.text)
        self.assertIn(self.post_001.content, post_area.text)

        self.assertIn(self.tag_django.name, post_area.text)
        self.assertNotIn(self.tag_python.name, post_area.text)
        self.assertNotIn(self.tag_python_kar.name, post_area.text)

    # 카테고리별 페이지 나타내는 함수
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

    # 태그 페이지를 나타내는 함수
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

    # 폼(form)을 이용한 포스트 작성 페이지 생성
    def test_create_post(self):  
        response = self.client.get('/blog/create_post/')
        self.assertEqual(response.status_code, 200)
        soup = BeautifulSoup(response.content, 'html.parser')

        self.assertEqual('Create Post - Blog', soup.title.text)
        main_area = soup.find('div', id='main-area')
        self.assertIn('Create a New Post', main_area.text)

