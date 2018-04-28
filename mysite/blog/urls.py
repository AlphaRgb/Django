#!/usr/bin/env python3
# coding:utf-8

from django.conf.urls import url,include
from . import views, views_base
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'posts',views.PostListViewSet)

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<post>[-\w]+)/$', views.post_detail, name='post_detail'),
    # url(r'posts/$', views.PostListView.as_view(), name='post-list'),
    url(r'^',include(router.urls))
]
