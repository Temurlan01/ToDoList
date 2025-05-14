from django.conf import settings
from django.db import models


class Task(models.Model):
    """Модель для заданий"""
    text = models.CharField(max_length=255)
    is_done = models.BooleanField(default=False)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='tasks',
        default=True
    )

    def __str__(self):
        return self.text


