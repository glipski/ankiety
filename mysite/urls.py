from django.contrib import admin
from django.conf.urls import url, include

admin.autodiscover()

urlpatterns = [
    url(r'^', include('polls.urls')),
    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^admin/', include(admin.site.urls)),
]
