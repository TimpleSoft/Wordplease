# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from blogs.api import PostViewSet
from rest_framework.routers import DefaultRouter
from api import APIBlogsListView


# APIRouter
router = DefaultRouter()
router.register(r'posts/(?P<username>[\w-]+)', PostViewSet)


urlpatterns = [
    # API Posts URLs
    url(r'1.0/', include(router.urls)),  # incluyo las URLS de API
    url(r'1.0/posts/$', APIBlogsListView.as_view(), name='api_blog_detail'), # para construir las urls de los blogs

    # API Blogs
    url(r'1.0/blogs/$', APIBlogsListView.as_view(), name='api_blogs_list')
]
