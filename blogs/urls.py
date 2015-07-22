# -*- coding: utf-8 -*-
from django.conf.urls import url
from views import HomeView, PostDetailView, BlogsListView, BlogDetailView, CreatePostView


urlpatterns = [
    # Posts URLs
    url(r'^$', HomeView.as_view(), name='blogs_home'),
    url(r'^blogs/$', BlogsListView.as_view(), name='blogs_list'),
    url(r'^blogs/(?P<username>[\w-]+)$', BlogDetailView.as_view(), name='blog_detail'),
    url(r'^blogs/(?P<username>[\w-]+)/(?P<pk>[0-9]+)$', PostDetailView.as_view(), name='post_detail'),
    url(r'^new-post/$', CreatePostView.as_view(), name='create_post')

]