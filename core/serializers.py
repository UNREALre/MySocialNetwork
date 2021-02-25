# -*- coding: utf-8 -*-

from rest_framework import serializers

from users.serializers import UserSerializer

from .models import Post, Like


class LikeSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.id')
    post = serializers.ReadOnlyField(source='post.id')

    def validate(self, attrs):
        user = self.context['request'].user
        post = self.context['request'].data['id']

        if Like.objects.filter(user=user, post=post).exists():
            raise serializers.ValidationError('User have already voted for the post.')

        return attrs

    class Meta:
        model = Like
        fields = ('id', 'user', 'post', )


class UnlikeSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.id')
    post = serializers.ReadOnlyField(source='post.id')

    class Meta:
        model = Like
        fields = ('id', 'user', 'post', )


class PostSerializer(serializers.ModelSerializer):
    author = UserSerializer()
    likes = LikeSerializer(many=True)

    class Meta:
        model = Post
        fields = ('id', 'created', 'updated', 'author', 'text', 'likes', )


class PostCreateUpdateSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Post
        fields = ('id', 'created', 'updated', 'author', 'text', )
        read_only_fields = ('created', 'updated', )
