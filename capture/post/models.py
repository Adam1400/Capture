from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    content = models.URLField()
    post_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.comment
