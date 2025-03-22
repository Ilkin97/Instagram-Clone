from rest_framework import serializers
from .models import Story
from users.serializers import UserSerializer

class StorySerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Story
        fields = ['id', 'user', 'image', 'video', 'created_at', 'expires_at']

class StoryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Story
        fields = ['image', 'video', 'expires_at']

    def create(self, validated_data):
        user = self.context['request'].user
        story = Story.objects.create(user=user, **validated_data)
        return story
