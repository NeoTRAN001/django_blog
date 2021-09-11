from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    order = models.IntegerField()
    create_at = models.DateTimeField(auto_now_add=True)
