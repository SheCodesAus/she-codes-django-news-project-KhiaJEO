from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    avatar = models.URLField(blank=True)
    Your_socials = models.URLField(blank=True)
    Location = models.CharField(max_length=50, blank=True)
    About_you = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return self.username

