# coding: utf-8

from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User

from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status

from accounts.serializers import AccountSerializer


class AccountCreateEnpoint(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = AccountSerializer

    def pre_save(self, obj):
        obj.set_password(self.request.DATA['password'])

    def post_save(self, obj, created=False):
        if created:
            Token.objects.get_or_create(user=obj)


class LoginEndpoint(APIView):
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        username = request.DATA.get('username', '')
        password = request.DATA.get('password', '')

        user = get_object_or_404(User, username=username)

        if not user.check_password(password):
            return Response({}, status.HTTP_400_BAD_REQUEST)

        token, _ = Token.objects.get_or_create(user=user)

        return Response({'token': token.key}, status.HTTP_200_OK)
