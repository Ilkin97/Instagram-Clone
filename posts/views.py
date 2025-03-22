from rest_framework import status, permissions, generics
from rest_framework.response import Response
from .models import Post, Comment, Like
from .serializers import PostSerializer, CommentSerializer, LikeSerializer
from rest_framework.permissions import IsAuthenticated


class PostListView(generics.ListAPIView):
    queryset = Post.objects.all().order_by('-created_at')  # En son postlar ilk sırada
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]  # Sadece giriş yapmış kullanıcılar erişebilir

    def get_queryset(self):
        # Followed users' posts (Followed users' postlarını getirme)
        user = self.request.user
        followed_users = user.profile.following.all()  # Kullanıcının takip ettiği kullanıcılar
        return Post.objects.filter(user__in=followed_users).order_by('-created_at')


class PostCreateView(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]  # Giriş yapmış kullanıcılar post oluşturabilir

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)  # Postu oluştururken, kullanıcıyı bağla


class PostDetailView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]


class PostDeleteView(generics.DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def perform_destroy(self, instance):
        # Sadece post sahibinin silmesine izin ver
        if instance.user == self.request.user:
            instance.delete()
        else:
            raise PermissionError("You do not have permission to delete this post.")
