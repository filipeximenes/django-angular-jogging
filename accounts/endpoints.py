# coding: utf-8

from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token

from accounts.serializers import AccountSerializer


class AccountCreateEnpoint(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = AccountSerializer

    def create(self, request, *args, **kwargs):
        response = super(AccountCreateEnpoint, self).create(request, *args, **kwargs)

        if hasattr(self, 'object'):
            self.object.set_password(request.DATA['password'])
            self.object.save()
            Token.objects.get_or_create(user=self.object)

        return response

