# coding: utf-8

from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token

from accounts.serializers import AccountSerializer


class AccountCreateEnpoint(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = AccountSerializer

    def pre_save(self, obj):
        obj.set_password(self.request.DATA['password'])

    def post_save(self, obj, created=False):
        if created:
            Token.objects.get_or_create(user=obj)
