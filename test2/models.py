from django.db import models
from test1.models import Post

class Comment(models.Model):
    title = models.CharField(max_length=50, unique=False)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='Comments')

    def __str__(self) -> str:
        return self.title

