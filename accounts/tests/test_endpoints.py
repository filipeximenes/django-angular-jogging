# coding: utf-8

from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

from rest_framework import status

from core.test.utils import BaseAPITestMixing
from accounts.endpoints import AccountCreateEnpoint, LoginEndpoint


class AccountCreateEnpointTests(BaseAPITestMixing):
    view_name = 'accounts-create'

    def setUp(self):
        super(AccountCreateEnpointTests, self).setUp()

        self.view = AccountCreateEnpoint.as_view()

        self.params = {
            'email': 'test@email.com',
            'username': 'username',
            'password': 'password',
        }

    def test_url(self):
        params = self.params

        response = self.client.post(reverse(self.view_name), params)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_response_status(self):
        params = self.params

        request = self.factory.post('', params)
        response = self.view(request)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_sets_user_password(self):
        params = self.params

        request = self.factory.post('', params)
        response = self.view(request)

        user = User.objects.get(username=params['username'])

        self.assertTrue(user.check_password(params['password']))
        self.assertEqual(response.data['password'], '')

    def test_does_not_create_user_if_password_is_not_set(self):
        params = self.params

        params['password'] = ''

        request = self.factory.post('', params)
        response = self.view(request)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_returns_auth_token(self):
        params = self.params

        request = self.factory.post('', params)
        response = self.view(request)

        self.assertNotEqual(response.data['token'], '')


class LoginEndpointTests(BaseAPITestMixing):
    view_name = 'login'

    def setUp(self):
        super(LoginEndpointTests, self).setUp()

        self.view = LoginEndpoint.as_view()

        self.params = {
            'username': self.username,
            'password': self.password,
        }

    def test_url(self):
        params = self.params

        response = self.client.post(reverse(self.view_name), params)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_response_status(self):
        params = self.params

        request = self.factory.post('', params)
        response = self.view(request)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_returns_token(self):
        params = self.params

        request = self.factory.post('', params)
        response = self.view(request)

        self.assertNotEqual(response.data['token'], '')

    def test_test_returns_404_if_username_does_not_exists(self):
        params = self.params

        params['username'] = '...'

        request = self.factory.post('', params)
        response = self.view(request)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_returns_400_if_invalid_password(self):
        params = self.params

        params['password'] = self.password + '1'

        request = self.factory.post('', params)
        response = self.view(request)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
