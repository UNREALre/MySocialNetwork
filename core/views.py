# -*- coding: utf-8 -*-

from rest_framework import permissions, viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from .models import Like, Post
from .serializers import LikeSerializer, PostSerializer, PostCreateUpdateSerializer, UnlikeSerializer


class PostPermissions(permissions.BasePermission):
    """Permissions for different actions with Post model."""

    def has_permission(self, request, view):
        if view.action in ['list', 'retrieve']:
            return request.user.is_anonymous
        elif view.action in ['create']:
            return request.user.is_authenticated
        elif view.action in ['update', 'partial_update', 'destroy']:
            if request.user.is_authenticated:
                try:
                    Post.objects.get(pk=view.kwargs['pk'], author=request.user)
                    return True
                except Post.DoesNotExist:
                    return False
            else:
                return False
        else:
            return False


class LikePermissions(permissions.BasePermission):
    """Permissions for different actions with Like model."""

    def has_permission(self, request, view):
        if view.action in ['create']:
            return request.user.is_authenticated
        elif view.action in ['destroy']:
            if request.user.is_authenticated:
                try:
                    post = get_object_or_404(Post, pk=view.kwargs['pk'])
                    return True if Like.objects.filter(post=post, user=request.user).exists() else False
                except Post.DoesNotExist:
                    return False
            else:
                return False
        else:
            return False


class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    permission_classes = [PostPermissions, ]
    queryset = Post.objects.all()

    def perform_create(self, serializer):
        return serializer.save(author=self.request.user)

    def perform_update(self, serializer):
        return serializer.save(author=self.request.user)

    def create(self, request, *args, **kwargs):
        self.serializer_class = PostCreateUpdateSerializer
        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        self.serializer_class = PostCreateUpdateSerializer
        return super().update(request, *args, **kwargs)


class LikeViewSet(viewsets.ModelViewSet):
    serializer_class = LikeSerializer
    permission_classes = [LikePermissions, ]
    queryset = Like.objects.all()
    http_method_names = ['post', 'delete', ]

    def perform_create(self, serializer):
        post = get_object_or_404(Post, id=self.request.data.get('id'))
        return serializer.save(user=self.request.user, post=post)

    def destroy(self, request, *args, **kwargs):
        post = Post.objects.get(id=kwargs.get('pk'))
        Like.objects.get(post=post, user=request.user).delete()
        return Response()

