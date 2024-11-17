from rest_framework import generics, permissions
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListAPIView
from .models import *
from .serializers import *
from .permissions import *

####################user and user profile###################################
class UserProfileView(generics.RetrieveUpdateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        profile, created = UserProfile.objects.get_or_create(user=self.request.user)
        return profile
    

class ListUserProfile(generics.ListCreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAdminUser]

class DetailUserProfile(generics.RetrieveDestroyAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAdminUser]


class ListUsers(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.IsAdminUser]

class DetailUser(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.IsAdminUser]


####################post and comment###################################
class ListPost(generics.ListCreateAPIView):
    serializer_class = PostListSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):    
        return Post.objects.filter(author__in=self.request.user.following.all() | CustomUser.objects.filter(id=self.request.user.id))

    
    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request 
        return context

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class DetailPost(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PostDetailSerializer
    permission_classes = (IsAdminOrAuthorOrReadOnly,)

    def get_queryset(self):
        return Post.objects.filter(author__in=self.request.user.following.all() | CustomUser.objects.filter(id=self.request.user.id))

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request 
        return context

class ListCreateComment(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Comment.objects.filter(post_id=self.kwargs["post_id"])

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, post_id=self.kwargs["post_id"])

class DetailComment(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (IsAuthorOrReadOnly,)

####################search###################################

class SearchProfilesView(ListAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    filter_backends = [SearchFilter]
    search_fields = ['user__username', 'bio']

###########following#########################################

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class FollowUser(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        user_to_follow = CustomUser.objects.get(id=user_id)
        if user_to_follow not in request.user.following.all():
            request.user.following.add(user_to_follow)
            return Response({"detail": "User followed."}, status=status.HTTP_200_OK)
        return Response({"detail": "Already following this user."}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, user_id):
        user_to_unfollow = CustomUser.objects.get(id=user_id)
        if user_to_unfollow in request.user.following.all():
            request.user.following.remove(user_to_unfollow)
            return Response({"detail": "User unfollowed."}, status=status.HTTP_200_OK)
        return Response({"detail": "Not following this user."}, status=status.HTTP_400_BAD_REQUEST)
