from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns('',
    url(r'^add_client/$', views.add_client, name='add_client'),
)