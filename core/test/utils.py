# coding: utf-8

from django.contrib.auth.models import User

from rest_framework.test import APITestCase, APIClient, APIRequestFactory
from rest_framework.authtoken.models import Token


class BaseAPITestMixing(APITestCase):

    def setUp(self):
        username = 'test'
        password = 'testpassword'
        self.user = User.objects.create_user(
            username, 'test@test.com', password)

        token = Token.objects.create(user=self.user)
        token.save()

        self.auth_client = APIClient()
        self.auth_client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

        self.factory = APIRequestFactory()
