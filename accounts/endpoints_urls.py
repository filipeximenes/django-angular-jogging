# coding: utf-8

from django.conf.urls import patterns, include, url

from accounts.endpoints import AccountCreateEnpoint, LoginEndpoint


urlpatterns = patterns('',
    url(r'^accounts/$', AccountCreateEnpoint.as_view(), name='accounts-create'),
    url(r'^login/$', LoginEndpoint.as_view(), name='login'),
)
