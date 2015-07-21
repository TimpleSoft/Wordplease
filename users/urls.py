# -*- coding: utf-8 -*-
from django.conf.urls import url
from views import BlogsListView


urlpatterns = [
    # Users URLs
    url(r'^blogs/$', BlogsListView.as_view(), name='blogs_list'),
]