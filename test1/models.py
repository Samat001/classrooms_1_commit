from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=50 , unique=False )
    descriptions = models.TextField(null=False)

    def __str__(self) -> str:
        return self.title


