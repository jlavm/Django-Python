from django.conf.urls import patterns, include, url
from django.contrib import admin
from phots import views,api
admin.autodiscover()



urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.HomeView.as_view()),
    url(r'^login$', views.UserLogin.as_view()),
    url(r'^logout$', views.UserLogout.as_view()),
    url(r'^profile$', views.UserProfile.as_view()),
    url(r'^phots$', views.PhotoListView.as_view()),
    url(r'^create$', 'phots.views.create_photo'),
    url(r'^photos/(?P<pk>[0-9]+)$', views.PhotoDetail.as_view()),


    #api urls
    url(r'^api/1.0/users/$', api.UserListApi.as_view()),
    url(r'^api/1.0/users/(?P<pk>[0-9]+)$', api.UserDetailApi.as_view()),
    #Photo api
    url(r'^api/1.0/photos/$', api.PhotoListApi.as_view()),

)
