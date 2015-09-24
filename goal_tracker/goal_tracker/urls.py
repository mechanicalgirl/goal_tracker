from django.conf.urls import include, url
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^$', include('goals.urls')),
    url(r'^goals/', include('goals.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
