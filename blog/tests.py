from django.test import TestCase, Client
from bs4 import BeautifulSoup
from .models import Post


class TestView(TestCase):
    def setUp(self):
        self.client = Client()

    def test_post_list(self):
        response = self.client.get('/blog/')
        self.assertEqual(response.status_code, 200)
        soup = BeautifulSoup(response.content, 'html.parser')
        self.assertIn('Blog', soup.title.text)

        navbar = soup.nav
        self.assertIn('Blog', navbar.text)
        self.assertIn('Blog', navbar.text)

        self.assertEqual(Post.objects.count(), 0)
        main_area = soup.find('div', id='main-area')
        self.assertIn('아직 게시물이 없습니다.', main_area.text)

        post_001 = Post.objects.create(
            title = "첫 번째 포스트 입니다.",
            content = "Hello World! We are the World",
        )
        
        post_002 = Post.objects.create(
            title = "두 번째 포스트 입니다.",
            content = "저는 마라탕과 떡볶이를 사랑합니다",
        )

        self.assertEqual(Post.objects.count(), 2)
        response =self.client.get('/blog/')
        soup = BeautifulSoup(response.content, 'html.parser')
        
        main_area = soup.find('div', id='main-area')
        self.assertIn(post_001.title, main_area.text)
        self.assertIn(post_002.title, main_area.text)
        