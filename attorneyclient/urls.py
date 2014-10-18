from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns('',
    url(r'^add_client/$', views.add_client, name='add_client'),
    url(r'^add_case/$', views.add_case, name='add_case'),
)