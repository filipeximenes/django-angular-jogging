# coding: utf-8

from django.conf.urls import patterns, include, url

from timings.endpoints import (
    TimingsListCreateEndpoint, TimingsRetrieveUpdateDestroyEndpoint)


urlpatterns = patterns('',
    url(r'^timings/$', TimingsListCreateEndpoint.as_view(), name='timings-list-create'),
    url(r'^timings/(?P<pk>\d+)/$', TimingsRetrieveUpdateDestroyEndpoint.as_view(), name='timings-retrive-update-destroy'),
)
