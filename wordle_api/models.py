from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    games_played = models.IntegerField(default=0)
    games_won = models.IntegerField(default=0)
    current_streak = models.IntegerField(default=0)
    max_streak = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username


class Word(models.Model):
    word = models.CharField(max_length=5, unique=True)

    def __str__(self):
        return self.word