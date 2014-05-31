from django.contrib.auth.models import User

from django.db import models


class UserProfile(models.Model):
    """Extra information to track for each user"""
    user = models.OneToOneField(User)

    pushover_key = models.CharField(max_length=256, help_text='account key from pushover')