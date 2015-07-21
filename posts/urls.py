# -*- coding: utf-8 -*-
from django.conf.urls import url
from views import HomeView


urlpatterns = [
    # Posts URLs
    url(r'', HomeView.as_view(), name="posts_home")
]