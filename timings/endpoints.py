# coding: utf-8

from rest_framework import generics

from timings.models import Timing
from timings.serializers import TimingsSerializer


class TimingsListCreateEndpoint(generics.ListCreateAPIView):
    model = Timing
    serializer_class = TimingsSerializer

    def get_queryset(self):
        user = self.request.user
        return super(TimingsListCreateEndpoint, self).get_queryset() \
            .filter(user=user)

    def create(self, request, *args, **kwargs):
        request.DATA['user'] = self.request.user.id
        return super(TimingsListCreateEndpoint, self).create(request, *args, **kwargs)


class TimingsRetrieveUpdateDestroyEndpoint(generics.RetrieveUpdateDestroyAPIView):
    model = Timing
    serializer_class = TimingsSerializer
