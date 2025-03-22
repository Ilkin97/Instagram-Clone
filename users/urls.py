from django.urls import path
from .views import UserRegisterView, UserLoginView, UserProfileView, FollowUserView


urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='user-register'),
    path('login/', UserLoginView.as_view(), name='user-login'),
    path('<str:username>/', UserProfileView.as_view(), name='user-profile'),
    path('<str:username>/follow/', FollowUserView.as_view(), name='follow-user'),
]