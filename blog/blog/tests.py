from django.test import TestCase

from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import Blog

class BlogModelTests(TestCase):
    
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="testuser",
            email="test@test.com",
            password="998887766test",
        )

        self.post = Blog.objects.create(
            title="Test post",
            description = "Test body",
            author=self.user,
        )

    
    def test_string_representation(self):
        post = Blog(title="Test post")
        self.assertEqual(str(post), post.title)
    
    def test_post_content(self):
        self.assertEqual(f"{self.post.title}", "Test post")
        self.assertEqual(f"{self.post.author}", "testuser")
        self.assertEqual(f"{self.post.description}", "Test body")