# coding: utf-8

from django.contrib.auth.models import User

from rest_framework import serializers
from rest_framework.authtoken.models import Token


class AccountSerializer(serializers.ModelSerializer):
    token = serializers.SerializerMethodField('get_auth_token')

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'token']

    def transform_password(self, obj, value):
        return ''

    def get_auth_token(self, obj):
        token, _ = Token.objects.get_or_create(user=obj)
        return token
