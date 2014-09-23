# coding: utf-8

from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

from rest_framework.test import APIRequestFactory, APITestCase, force_authenticate, APIClient
from rest_framework import status
from model_mommy import mommy

from timings.endpoints import (
    TimingsListCreateEndpoint, TimingsRetrieveUpdateDestroyEndpoint)


factory = APIRequestFactory()


class BaseAPITestMixing(APITestCase):

    def setUp(self):
        username = 'test'
        password = 'testpassword'
        self.user = User.objects.create_user(
            username, 'test@test.com', password)

        self.auth_client = APIClient()
        self.auth_client.login(username=username, password=password)


class ListTimingsEndpointTests(BaseAPITestMixing):
    view_name = 'timings-list-create'

    def setUp(self):
        super(ListTimingsEndpointTests, self).setUp()

        self.view = TimingsListCreateEndpoint.as_view()

    def test_url(self):
        response = self.auth_client.get(reverse(self.view_name))

        self.assertEqual(response.status_code, status.HTTP_200_OK)

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

        mommy.make('timings.Timing', user=user, _quantity=2)

        request = factory.get('')
        force_authenticate(request, user=user)
        response = self.view(request)

        self.assertEqual(len(response.data), 2)

    def test_only_returns_auth_user_timings(self):
        user = self.user

        mommy.make('timings.Timing')

        request = factory.get('')
        force_authenticate(request, user=user)
        response = self.view(request)

        self.assertEqual(len(response.data), 0)


class CreateTimingsEndpointTests(BaseAPITestMixing):
    view_name = 'timings-list-create'

    def setUp(self):
        super(CreateTimingsEndpointTests, self).setUp()

        self.view = TimingsListCreateEndpoint.as_view()

        self.params = {
            'time': '1:23:34',
            'distance': 10500,
            'date': '2014-09-21'
        }

    def test_url(self):
        params = self.params

        response = self.auth_client.post(reverse(self.view_name), params)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_response_status(self):
        user = self.user
        params = self.params

        request = factory.post('', params)
        force_authenticate(request, user=user)
        response = self.view(request)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_cannot_create_timing_for_different_user(self):
        user = self.user
        params = self.params

        other_user = mommy.make('auth.User')
        params['user'] = other_user.id

        request = factory.post('', params)
        force_authenticate(request, user=user)
        response = self.view(request)

        self.assertEqual(response.data['user'], user.id)

    def test_returns_created_timing_id(self):
        user = self.user
        params = self.params

        request = factory.post('', params)
        force_authenticate(request, user=user)
        response = self.view(request)

        self.assertIn('id', response.data)


class RetrieveTimingsEndpointTests(BaseAPITestMixing):
    view_name = 'timings-retrive-update-destroy'

    def setUp(self):
        super(RetrieveTimingsEndpointTests, self).setUp()

        self.view = TimingsRetrieveUpdateDestroyEndpoint.as_view()

        self.timing = mommy.make('timings.Timing', user=self.user)

    def test_url(self):
        timing = self.timing

        response = self.auth_client.get(reverse(self.view_name, kwargs={'pk': timing.pk}))

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_response_status(self):
        user = self.user
        timing = self.timing

        request = factory.get('')
        force_authenticate(request, user=user)
        response = self.view(request, pk=timing.pk)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_only_retrieve_self_timings(self):
        user = self.user

        other_timing = mommy.make('timings.Timing')

        request = factory.get('')
        force_authenticate(request, user=user)
        response = self.view(request, pk=other_timing.pk)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class UpdateTimingsEndpointTests(BaseAPITestMixing):
    view_name = 'timings-retrive-update-destroy'

    def setUp(self):
        super(UpdateTimingsEndpointTests, self).setUp()

        self.view = TimingsRetrieveUpdateDestroyEndpoint.as_view()

        self.timing = mommy.make('timings.Timing', user=self.user)

        self.params = {
            'time': '1:23:34',
            'distance': 10500,
            'date': '2014-09-21'
        }

    def test_url(self):
        timing = self.timing
        params = self.params

        response = self.auth_client.put(reverse(self.view_name, kwargs={'pk': timing.pk}), params)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_response_status(self):
        user = self.user
        timing = self.timing
        params = self.params

        request = factory.put('', params)
        force_authenticate(request, user=user)
        response = self.view(request, pk=timing.pk)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_updates_distance(self):
        user = self.user
        timing = self.timing
        params = self.params

        request = factory.put('', params)
        force_authenticate(request, user=user)
        response = self.view(request, pk=timing.pk)

        self.assertEqual(response.data['distance'], params['distance'])

    def test_can_only_update_self_timings(self):
        user = self.user
        params = self.params

        other_timing = mommy.make('timings.Timing')

        request = factory.put('', params)
        force_authenticate(request, user=user)
        response = self.view(request, pk=other_timing.pk)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class DestroyTimingsEndpointTests(BaseAPITestMixing):
    view_name = 'timings-retrive-update-destroy'

    def setUp(self):
        super(DestroyTimingsEndpointTests, self).setUp()

        self.view = TimingsRetrieveUpdateDestroyEndpoint.as_view()

        self.timing = mommy.make('timings.Timing', user=self.user)

    def test_url(self):
        timing = self.timing

        response = self.auth_client.delete(reverse(self.view_name, kwargs={'pk': timing.pk}))

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_response_status(self):
        user = self.user
        timing = self.timing

        request = factory.delete('')
        force_authenticate(request, user=user)
        response = self.view(request, pk=timing.pk)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_can_only_destroy_self_timings(self):
        user = self.user

        other_timing = mommy.make('timings.Timing')

        request = factory.delete('')
        force_authenticate(request, user=user)
        response = self.view(request, pk=other_timing.pk)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
