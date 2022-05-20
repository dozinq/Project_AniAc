from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class User(AbstractUser):
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')


