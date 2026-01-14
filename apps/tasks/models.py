from django.db import models
from apps.users.models import User


class Task(models.Model):
    title = models.CharField()
    description = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)