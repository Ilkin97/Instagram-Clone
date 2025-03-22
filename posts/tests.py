from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from users.models import CustomUser
from posts.models import Post, Like, Comment
from django.contrib.auth import get_user_model


class PostCreationTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = CustomUser.objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='testpassword123'
        )
        self.client.force_authenticate(user=self.user)
        self.url = reverse('post-create')

    def test_create_post(self):
        data = {
            'image': 'image_url_or_file',
            'caption': 'This is a test post',
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Post.objects.count(), 1)
        self.assertEqual(Post.objects.get().caption, 'This is a test post')


class PostListTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = CustomUser.objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='testpassword123'
        )
        self.client.force_authenticate(user=self.user)
        self.url = reverse('post-list')

        Post.objects.create(user=self.user, caption='Post 1', image='image_url_1')
        Post.objects.create(user=self.user, caption='Post 2', image='image_url_2')

    def test_post_list(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)


class PostDeleteTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = CustomUser.objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='testpassword123'
        )
        self.client.force_authenticate(user=self.user)
        self.post = Post.objects.create(user=self.user, caption='Post to delete', image='image_url')

    def test_delete_post(self):
        url = reverse('post-delete', kwargs={'pk': self.post.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Post.objects.count(), 0)


class LikePostTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = CustomUser.objects.create_user(
            username='testuser',
        )
        self.client.force_authenticate(user=self.user)
        self.post = Post.objects.create(user=self.user, caption='Post to like', image='image_url')
        
    def test_like_post(self):
        url = reverse('post-like', kwargs={'pk': self.post.pk})
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Like.objects.count(), 1)
        

class CommentPostTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = CustomUser.objects.create_user(
            username='testuser',
        )
        self.client.force_authenticate(user=self.user)
        self.post = Post.objects.create(user=self.user, caption='Post to comment', image='image_url')
        
    def test_comment_post(self):
        url = reverse('post-comment', kwargs={'pk': self.post.pk})
        data = {
            'text': 'This is a test comment'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Comment.objects.count(), 1)
        self.assertEqual(Comment.objects.get().text, 'This is a test comment')