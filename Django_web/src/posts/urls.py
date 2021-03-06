from django.conf.urls import url
from django.contrib import admin
from posts.views import post_create, post_list, post_detail, post_update, post_delete

urlpatterns = [
    url(r'^$', post_list, name='list'),  # Posts url Default
    url(r'^create/$', post_create),
    url(r'^list/$', post_list),
    url(r'^(?P<slug>[\w-]+)/$', post_detail, name='detail'),
    url(r'^(?P<slug>[\w-]+)/edit/$', post_update, name='update'),
    url(r'^(?P<slug>[\w-]+)/delete/$', post_delete),
]