from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from users.models import CustomUser
from stories.models import Story
from django.contrib.auth import get_user_model


class StoryCreationTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = CustomUser.objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='testpassword123'
        )
        self.client.force_authenticate(user=self.user)
        self.url = reverse('story-create')

    def test_create_story(self):
        data = {
            'image': 'image_url_or_file',
            'expires_at': '2025-03-23T10:00:00Z',
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Story.objects.count(), 1)
        self.assertEqual(Story.objects.get().expires_at, '2025-03-23T10:00:00Z')


class StoryListTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = CustomUser.objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='testpassword123'
        )
        self.client.force_authenticate(user=self.user)
        self.url = reverse('story-list')

        Story.objects.create(user=self.user, image='story_image_1', expires_at='2025-03-23T10:00:00Z')
        Story.objects.create(user=self.user, image='story_image_2', expires_at='2025-03-23T11:00:00Z')

    def test_story_list(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
