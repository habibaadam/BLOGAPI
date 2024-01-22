from django.db import models
from django.utils import timezone

# . Create Models:
#   - Design Django models for:
#       - Blog post (fields: title, content, author, timestamp).
#       - Comment (fields: commenter name, content, timestamp).

class Post(models.Model):
    """Model representing the blog post and its fields"""
    title = models.CharField(max_length = 100)
    content = models.TextField()
    author = models.CharField(max_length = 100)
    timestamp = models.DateTimeField(default = timezone.now)

class Comment(models.Model):
    """Model representing the comment and its fields"""
    commenter_name = models.CharField(max_length = 100)
    content = models.TextField()
    timestamp = models.DateTimeField(default = timezone.now)
