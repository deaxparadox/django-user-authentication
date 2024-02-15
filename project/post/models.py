from django.db import models

from user_auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=250)
    description = models.CharField(max_length=500, blank=True, null=True)
    detail = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    user = models.ForeignKey(User, related_name="post", on_delete=models.CASCADE)
    