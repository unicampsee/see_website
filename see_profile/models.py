from django.db import models
from django.utils.crypto import get_random_string
from django.contrib.auth.models import User
from maro_auth.email_helpers import welcome_email, send_change_email

# Create your models here.

class ProfileUser(models.Model):
    user = models.OneToOneField(
            User,
            on_delete=models.CASCADE
        )

    def __str__(self):
        return self.user.username

