# -*- coding: utf-8 -*-
from django.conf.urls import url
from views import HomeView, DetailView, BlogsListView, BlogDetailView


urlpatterns = [
    # Posts URLs
    url(r'^$', HomeView.as_view(), name='posts_home'),
    url(r'^blogs/$', BlogsListView.as_view(), name='blogs_list'),
    url(r'^blogs/(?P<username>[\w-]+)$', BlogDetailView.as_view(), name='blog_detail'),
    url(r'^post/(?P<pk>[0-9]+)$', DetailView.as_view(), name='post_detail'),

]