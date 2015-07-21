from django.conf.urls import include, url
from django.contrib import admin
from posts import urls as posts_urls

urlpatterns = [

    url(r'^admin/', include(admin.site.urls)),

    # Posts URLs
    url(r'', include(posts_urls)),

]
