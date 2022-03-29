from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Task(models.Model):
    """Task model."""

    owner: models.ForeignKey = models.ForeignKey(
        User, null=True, blank=True, on_delete=models.CASCADE
    )
    title: models.CharField = models.CharField(max_length=100)
    completed: models.BooleanField = models.BooleanField(default=False)
    description: models.CharField = models.CharField(max_length=3000, blank=True)
    created: models.DateTimeField = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title
