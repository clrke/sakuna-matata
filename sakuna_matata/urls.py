from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^api/', include('api.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^channels/(?P<name>.*)', 'sakuna_matata.views.home', name='home'),
]
