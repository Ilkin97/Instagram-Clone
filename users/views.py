from rest_framework import generics
from rest_framework.response import Response
from .models import CustomUser
from .serializers import UserSerializer, UserRegisterSerializer, UserLoginSerializer
from rest_framework.permissions import IsAuthenticated


class UserRegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserRegisterSerializer


class UserLoginView(generics.GenericAPIView):
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data)


class UserProfileView(generics.RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'username'


class FollowUserView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        user_to_follow = CustomUser.objects.get(username=kwargs['username'])
        user = request.user
        if user == user_to_follow:
            return Response({"detail": "You cannot follow yourself."}, status=400)
        
        if user_to_follow in user.following.all():
            user.following.remove(user_to_follow)
            return Response({"detail": f"Unfollowed {user_to_follow.username}"})
        else:
            user.following.add(user_to_follow)
            return Response({"detail": f"Followed {user_to_follow.username}"})
