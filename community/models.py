from django.db import models
from django.conf import settings
import datetime


class Review(models.Model):
    title = models.CharField(max_length=100)
    movie_title = models.CharField(max_length=50, blank=True, null=True)
    rank = models.IntegerField(blank=True, null=True)
    content = models.TextField()
    created_at = models.DateTimeField(default=datetime.datetime.now)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_reviews')


class Comment(models.Model):
    content = models.TextField(max_length=200)
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=datetime.datetime.now)
