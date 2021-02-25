# -*- coding: utf-8 -*-

from django.contrib import admin

from .models import Post, Like


class PostAdmin(admin.ModelAdmin):
    pass


class LikeAdmin(admin.ModelAdmin):
    pass


admin.site.register(Post, PostAdmin)
admin.site.register(Like, LikeAdmin)
