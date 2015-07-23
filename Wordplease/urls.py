from django.conf.urls import include, url
from django.contrib import admin
from blogs import urls as blogs_urls, api_urls as blogs_api_urls
from users import urls as users_urls, api_urls as users_api_urls

urlpatterns = [

    url(r'^admin/', include(admin.site.urls)),

    # Blogs URLs
    url(r'', include(blogs_urls)),
    url(r'api/', include(blogs_api_urls)),

    # Users URLs
    url(r'', include(users_urls)),
    url(r'api/', include(users_api_urls))

]
