from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Story
from .serializers import StorySerializer, StoryCreateSerializer
from datetime import timedelta
from django.utils import timezone


class StoryUploadView(generics.CreateAPIView):
    serializer_class = StoryCreateSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        expires_at = timezone.now() + timedelta(hours=24)
        serializer.save(expires_at=expires_at, user=self.request.user)

class StoryListView(generics.ListAPIView):
    serializer_class = StorySerializer

    def get_queryset(self):
        return Story.objects.filter(user__in=self.request.user.following.all(), expires_at__gt=timezone.now())
