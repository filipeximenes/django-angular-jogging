# coding: utf-8

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from core.permissions import CustomViewPermission
from timings.models import Timing
from timings.serializers import TimingSerializer, TimingUpdateSerializer
from timings.filters import TimingFilter


class TimingsListCreateEndpoint(generics.ListCreateAPIView):
    model = Timing
    serializer_class = TimingSerializer
    filter_class = TimingFilter

    def get_queryset(self):
        user = self.request.user
        return super(TimingsListCreateEndpoint, self).get_queryset() \
            .filter(user=user)

    def create(self, request, *args, **kwargs):
        request.DATA['user'] = self.request.user.id
        return super(TimingsListCreateEndpoint, self).create(request, *args, **kwargs)


class TimingsRetrieveUpdateDestroyEndpoint(generics.RetrieveUpdateDestroyAPIView):
    model = Timing
    serializer_class = TimingSerializer
    permission_classes = (IsAuthenticated, CustomViewPermission)

    def custom_object_permission(self, request, obj=None):
        return request.user == obj.user

    def update(self, request, *args, **kwargs):
        self.serializer_class = TimingUpdateSerializer
        return super(TimingsRetrieveUpdateDestroyEndpoint, self).update(request, *args, **kwargs)
