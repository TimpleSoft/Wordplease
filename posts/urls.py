# -*- coding: utf-8 -*-
from django.conf.urls import url
from views import HomeView, DetailView


urlpatterns = [
    # Posts URLs
    url(r'^$', HomeView.as_view(), name='posts_home'),
    url(r'^post/(?P<pk>[0-9]+)$', DetailView.as_view(), name='post_detail'),
]