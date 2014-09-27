# coding: utf-8

from django.conf.urls import patterns, include, url

from accounts.endpoints import AccountCreateEnpoint


urlpatterns = patterns('',
    url(r'^accounts/$', AccountCreateEnpoint.as_view(), name='accounts-create'),
)
