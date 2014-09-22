# coding: utf-8

from rest_framework import generics

from timings.models import Timings
from timings.serializers import TimingsSerializer


class TimingsListCreateEndpoint(generics.ListCreateAPIView):
    model = Timings
    serializer_class = TimingsSerializer

    def get_queryset(self):
        user = self.request.user
        return super(TimingsListCreateEndpoint, self).get_queryset() \
            .filter(user=user)