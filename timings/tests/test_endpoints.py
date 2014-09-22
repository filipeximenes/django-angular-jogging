# coding: utf-8

from django.contrib.auth.models import User

from rest_framework.test import APIRequestFactory, APITestCase, force_authenticate
from rest_framework import status
from model_mommy import mommy

from timings.endpoints import TimingsListCreateEndpoint


factory = APIRequestFactory()


class BaseAPITestMixing(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            'test', 'test@test.com', 'testpassword')


class ListTimingsEndpointTests(BaseAPITestMixing):

    def setUp(self):
        super(ListTimingsEndpointTests, self).setUp()

        self.view = TimingsListCreateEndpoint.as_view()

    def test_response_status(self):
        user = self.user

        request = factory.get('')
        force_authenticate(request, user=user)
        response = self.view(request)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_requires_logged_user(self):
        request = factory.get('')
        response = self.view(request)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_response_content(self):
        user = self.user

        mommy.make('timings.Timings', user=user, _quantity=2)

        request = factory.get('')
        force_authenticate(request, user=user)
        response = self.view(request)

        self.assertEqual(len(response.data), 2)

    def test_only_returns_auth_user_timings(self):
        user = self.user

        mommy.make('timings.Timings')

        request = factory.get('')
        force_authenticate(request, user=user)
        response = self.view(request)

        self.assertEqual(len(response.data), 0)
