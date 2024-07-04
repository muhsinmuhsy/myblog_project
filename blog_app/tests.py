from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from rest_framework.authtoken.models import Token
from .models import Post, Comment

# Create your tests here.

class UserTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_user_registration(self):
        response = self.client.post('/api/users/register/', {
            'username': 'testuser',
            'password': 'testpassword123',
            'email': 'testuser@example.com'
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('token', response.data)
        print(f"List Register Response Data: {response.data}")

    def test_user_login(self):
        user = User.objects.create_user(username='testuser', password='testpassword123')
        response = self.client.post('/api/users/login/', {
            'username': 'testuser',
            'password': 'testpassword123'
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('token', response.data)
        print(f"List Login Response Data: {response.data}")

    def test_user_logout(self):
        user = User.objects.create_user(username='testuser', password='testpassword123')
        token = Token.objects.create(user=user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        response = self.client.post('/api/users/logout/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(f"List Logout Data: {response.data}")


class PostTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpassword123')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test_create_post(self):
        response = self.client.post('/api/posts/', {
            'title': 'Test Post',
            'content': 'This is a test post.'
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        print(f"Create Post Response Data: {response.data}")

    def test_list_posts(self):
        Post.objects.create(title='Test Post', content='This is a test post.', author=self.user)
        response = self.client.get('/api/posts/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(f"List Posts Response Data: {response.data}")

    def test_update_post(self):
        post = Post.objects.create(title='Test Post', content='This is a test post.', author=self.user)
        response = self.client.put(f'/api/posts/{post.id}/', {
            'title': 'Updated Post',
            'content': 'This is an updated test post.'
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(f"Update Post Response Data: {response.data}")

    def test_delete_post(self):
        post = Post.objects.create(title='Test Post', content='This is a test post.', author=self.user)
        response = self.client.delete(f'/api/posts/{post.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        print(f"Delete Post Data: {response.data}")


class CommentTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpassword123')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        self.post = Post.objects.create(title='Test Post', content='This is a test post.', author=self.user)

    def test_create_comment(self):
        response = self.client.post('/api/comments/', {
            'post': self.post.id,
            'content': 'This is a test comment.'
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        print(f"Create Comment Response Data: {response.data}")

    def test_list_comments(self):
        Comment.objects.create(post=self.post, content='This is a test comment.', author=self.user)
        response = self.client.get('/api/comments/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(f"List Comments Response Data: {response.data}")

    def test_update_comment(self):
        comment = Comment.objects.create(post=self.post, content='This is a test comment.', author=self.user)
        response = self.client.put(f'/api/comments/{comment.id}/', {
            'post': self.post.id,
            'content': 'This is an updated test comment.'
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(f"Update Comment Response Data: {response.data}")

    def test_delete_comment(self):
        comment = Comment.objects.create(post=self.post, content='This is a test comment.', author=self.user)
        response = self.client.delete(f'/api/comments/{comment.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        print(f"Delete Comment Data: {response.data}")
