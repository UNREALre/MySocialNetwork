# -*- coding: utf-8 -*-

from django.conf import settings
from django.contrib.auth import get_user_model
from rest_framework import serializers

from core.errors import SN_ERRORS
from core.utils import is_email_valid, enrich_user_by_email

UserModel = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ('id', 'username', 'password', 'first_name', 'last_name', 'email', 'location', 'city', 'state',
                  'country', 'bio', 'site')

    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        if settings.VERIFY_EMAILS:
            if not is_email_valid(attrs['email']):
                raise serializers.ValidationError(SN_ERRORS.get('not_valid_email'))

        return attrs

    def create(self, validated_data):
        enriched_data = enrich_user_by_email(validated_data['email'])

        person = enriched_data['person'] if enriched_data else {}
        geo = person['geo'] if person else {}

        user = UserModel.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email'],
            location=person.get('location'),
            city=geo.get('city'),
            state=geo.get('state'),
            country=geo.get('country'),
            bio=person.get('bio'),
            site=person.get('site'),
        )

        return user
