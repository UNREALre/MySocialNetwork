# -*- coding: utf-8 -*-

from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    """Custom User model."""

    # Data that we will try to get from clearbit. Full available data: https://clearbit.com/docs#enrichment-api
    location = models.CharField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    state = models.CharField(max_length=100, null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    site = models.CharField(max_length=200, null=True, blank=True)
