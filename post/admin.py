from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, Post, Comment, UserProfile

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ["email", "username", "name", "is_staff", "follower_count",'following_count']
    filter_horizontal = ('following',)  

    def follower_count(self, obj):
        return obj.followers.count()
    follower_count.short_description = "Followers"

    def following_count(self, obj):
        return obj.following.count()

    fieldsets = (
        (None, {"fields": ("username", "password")}),
        ("Personal info", {"fields": ("name", "email")}),
        ("Follow Info", {"fields": ("following",)}), 
        ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")}),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )
    
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("username", "name", "password1", "password2", "email"),
        }),
    )


admin.site.register(CustomUser, CustomUserAdmin)


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'bio']

admin.site.register(UserProfile, UserProfileAdmin)


class PostAdmin(admin.ModelAdmin):
    list_display = ['title','author']

admin.site.register(Post, PostAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ['post','author','body']

admin.site.register(Comment, CommentAdmin)