from django.conf.urls import include, patterns, url
from . import views
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^add_client/$', views.add_client, name='add_client'),
    url(r'^add_case/$', views.add_case, name='add_case'),
    url(r'^survey/', include('forms.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
