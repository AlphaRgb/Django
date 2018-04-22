#!/usr/bin/env python3
# coding=utf-8

from django.conf.urls import url,include

from . import views,api,mobile_views 
from rest_framework.documentation import include_docs_urls

from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'books',views.BookListViewSet,base_name='books')

# books_list = views.BookListViewSet.as_view({
# 		'get':'list',
# 		# 'post':'create'
# 	})

app_name = 'blogs'
urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'post/(?P<pk>[0-9]+)/$',views.detail,name='detail'),
    # url(r'api/books/',api.book_list,name='books'),
    # url(r'api/books/',books_list,name='books'),
    url(r'api/m/books/',mobile_views.book_list,name='mobile_books'),
    # url(r'docs/',include_docs_urls(title='blogs')),
    url(r'^api/',include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]