from django.urls import path
from .views import *



urlpatterns = [
    path('users/', ListUsers.as_view(), name='user-list'),
    path('users/<int:pk>/', DetailUser.as_view(), name='user-detail'),
    path('profile/', UserProfileView.as_view(), name='user-profile'),
    path('all-profiles/', ListUserProfile.as_view(), name='profile-list'),
    path('all-profiles/<int:pk>/', DetailUserProfile.as_view(), name='profile-detail'),
    path('feed/', ListPost.as_view(), name='post-list'),
    path('feed/<int:pk>/', DetailPost.as_view(), name='post-detail'),
    path('feed/<int:post_id>/comments/', ListCreateComment.as_view(), name='post-comments'),
    path('feed/<int:post_id>/comments/<int:pk>/', DetailComment.as_view(), name='comment-detail'),
    path('users/<int:user_id>/follow/', FollowUser.as_view(), name='follow-user'),
    path('search/', SearchProfilesView.as_view(), name='search-posts'),
]

