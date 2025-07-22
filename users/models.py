from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    color = models.CharField(max_length=7, default="#3AB2F4", verbose_name="Цвет событий (HEX)")

    def __str__(self):
        return f"Профиль {self.user.username}"
