from rest_framework import serializers
from .models import *



class CommentSerializer(serializers.ModelSerializer):
    commenter_name = serializers.CharField(source="author.name", read_only=True)
    post_title = serializers.CharField(source="post.title", read_only=True)

    class Meta:
        model = Comment
        fields = ['id','post_title', 'commenter_name', 'body', 'created_at']

class PostListSerializer(serializers.ModelSerializer):
    author_name = serializers.SerializerMethodField()
    comment_count = serializers.IntegerField(source='comments.count', read_only=True)

    class Meta:
        model = Post
        fields = ['title', 'body','image', 'author_name', 'comment_count']

    def get_author_name(self, obj):
        return obj.author.name if obj.author else "Anonymous"

    def create(self, validated_data):
        request = self.context.get('request')  
        validated_data['author'] = request.user  
        return super().create(validated_data)
    
class PostDetailSerializer(serializers.ModelSerializer):
    author_name = serializers.SerializerMethodField()
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'title', 'body', 'author_name', 'comments']

    def get_author_name(self, obj):
        return obj.author.name if obj.author else "Anonymous"


class UserProfileSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    posts = PostListSerializer(source='user.post_set.all', many=True) 
    profile_picture = serializers.ImageField(use_url=True)


    class Meta:
        model = UserProfile
        fields = ['user','bio', 'profile_picture', 'posts','profile_picture']



class CustomUserSerializer(serializers.ModelSerializer):
    profile = UserProfileSerializer()


    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'name', 'profile','profile_picture']
