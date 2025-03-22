from rest_framework import status, permissions, generics
from rest_framework.response import Response
from .models import Post, Comment, Like
from .serializers import PostSerializer, CommentSerializer, LikeSerializer
from rest_framework.permissions import IsAuthenticated
from django.http import HttpResponseServerError
import logging


# logger = logging.getLogger(__name__)

# def my_view(request):
#     try:
#         logger.info('ERROR: This is an info message')
#     except Exception as e:
#         logger.error(f'ERROR: {str(e)}')
#         return HttpResponseServerError("HTTP 500 Internal Server Error")


class PostListView(generics.ListAPIView):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        followed_users = user.profile.following.all()
        return Post.objects.filter(user__in=followed_users).order_by('-created_at')
    

class PostCreateView(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class PostDetailView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]


class PostDeleteView(generics.DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def perform_destroy(self, instance):
        if instance.user == self.request.user:
            instance.delete()
        else:
            raise PermissionError("You do not have permission to delete this post.")
