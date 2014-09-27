# coding: utf-8

from django.contrib.auth.models import User

from rest_framework import serializers


class AccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def transform_password(self, obj, value):
        return ''
