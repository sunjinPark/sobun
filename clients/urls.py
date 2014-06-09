from django.conf.urls import patterns, include, url
from clients.views import *
from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'EightFookCourt.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^display', display),

    # url(r'^manager/', ),
    )