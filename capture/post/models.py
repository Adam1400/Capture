from django.db import models
<<<<<<< Updated upstream
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    content = models.URLField()
    post_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.comment
=======
from django.contrib.auth.models import User


class Author(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.pk}. {self.name} {self.user.email}'


class Picture(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.pk}. {self.picName} by {self.author.name}'
>>>>>>> Stashed changes
