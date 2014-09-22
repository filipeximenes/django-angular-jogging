# coding: utf-8

from rest_framework import generics

from timings.models import Timings


class TimingsListCreateEndpoint(generics.ListCreateAPIView):
    model = Timings
