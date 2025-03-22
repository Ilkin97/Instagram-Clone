from django.urls import path
from .views import StoryUploadView, StoryListView

urlpatterns = [
    path('create/', StoryUploadView.as_view(), name='story-create'),
    path('', StoryListView.as_view(), name='story-list'),
]
