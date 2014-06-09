from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView
from users.views import *


admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'EightFookCourt.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^home', main),
    url(r'^join', signup),
    url(r'^login', login),
    )