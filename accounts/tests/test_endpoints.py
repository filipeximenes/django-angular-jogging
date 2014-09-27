# coding: utf-8

from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

from rest_framework import status

from core.test.utils import BaseAPITestMixing
from accounts.endpoints import AccountCreateEnpoint


class AccountCreateEnpointTests(BaseAPITestMixing):

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

        response = self.auth_client.post(reverse('accounts-create'), params)

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
