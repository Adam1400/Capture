from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    user = models.ForeignKey(User, unique=False, on_delete=models.CASCADE, default='0002')
    comment = models.TextField()
    content = models.ImageField(default='placeholder.jpg', upload_to='post_pics')
    post_date = models.DateTimeField(default=timezone.now)
    likes = models.ManyToManyField(User, related_name="user_likes")

    def __str__(self):
        return self.comment

    
