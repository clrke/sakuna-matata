from django.conf.urls import include, url

urlpatterns = [
    url(r'^$', 'api.v1.views.home', name='home'),
]
