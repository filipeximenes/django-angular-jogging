# coding: utf-8

from django.conf.urls import patterns, include, url

from timings.endpoints import TimingsListCreateEndpoint


urlpatterns = patterns('',
    url(r'^timings/$', TimingsListCreateEndpoint.as_view(), name='timings-list-create'),
)
