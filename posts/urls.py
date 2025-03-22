from django.urls import path
from .views import PostListView, PostCreateView, PostDetailView, PostDeleteView


urlpatterns = [
    path('', PostListView.as_view(), name='post-list'),  # Post listeleme
    path('create/', PostCreateView.as_view(), name='post-create'),  # Post oluşturma
    path('<int:pk>/', PostDetailView.as_view(), name='post-detail'),  # Post detayını gösterme
    path('<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),  # Post silme
]
