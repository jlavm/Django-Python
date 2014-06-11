from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
    url(r'^HellWorld$', 'phots.views.home'),
    url(r'^$', 'phots.views.home2'),
    url(r'^photos/(?P<pk>[0-9]+)$', 'phots.views.photo_detail')
)
