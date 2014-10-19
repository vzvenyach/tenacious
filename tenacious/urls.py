from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:

    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
    url('', include('django.contrib.auth.urls')),
    url(r'^$', 'tenacious.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^start/', include('attorneyclient.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
