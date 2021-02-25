# -*- coding: utf-8 -*-

from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()


class Post(models.Model):
    author = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='posts')
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created', ]


class Like(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')

    class Meta:
        unique_together = ('user', 'post')
