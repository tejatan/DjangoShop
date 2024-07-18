from django.conf import settings
from django.db import models

class Preferences(models.Model):
    THEMES = (
        ('light', 'Light Theme'),
        ('dark', 'Dark Theme'),
    )

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    theme = models.CharField(max_length=10, choices=THEMES, default='light')

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user'], name='unique_user_preference')
        ]


