from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.exceptions import ValidationError



class CustomUser(AbstractUser):
    name = models.CharField(null=True, blank=True, max_length=100)
    following = models.ManyToManyField("self", symmetrical=False, related_name="followers", blank=True)


    def clean(self):
        super().clean()
        if self.pk and self in self.following.all():  # Check if the user is saved
            raise ValidationError("You cannot follow yourself.")

    def save(self, *args, **kwargs):
        self.clean()  
        super().save(*args, **kwargs)

    

class Post(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='post_pics/', blank=True)
    body = models.TextField()


    def __str__(self):
        return self.title
    

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.author} - {self.body[:20]}"
        

class UserProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name="profile")
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    posts = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="posts", blank=True, null=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"