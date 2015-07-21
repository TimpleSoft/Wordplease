from django.conf.urls import include, url
from django.contrib import admin
from posts import urls as posts_urls
from users import urls as users_urls

urlpatterns = [

    url(r'^admin/', include(admin.site.urls)),

    # Posts URLs
    url(r'', include(posts_urls)),

    # Users URLs
    url(r'', include(users_urls)),

]
