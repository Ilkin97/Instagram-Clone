from django.db import models
from django.contrib.auth.models import User


class Story(models.Model):
    image = models.ImageField(upload_to='media/stories/images/', null=True, blank=True)
    video = models.FileField(upload_to='media/stories/videos/', blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField()
    expired = models.BooleanField(default=False)

    def __str__(self):
        return f"Story by {self.user.username}"
