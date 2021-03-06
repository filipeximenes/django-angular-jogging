from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', include('core.urls')),

    url(r'^api/', include('timings.endpoints_urls')),
    url(r'^api/', include('accounts.endpoints_urls')),
)
