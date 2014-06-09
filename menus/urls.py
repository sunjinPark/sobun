from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView
from menus.views import *


admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'EightFookCourt.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^manager/$', menu_control),
    url(r'^manager/insert/$', insert_page),
    url(r'^manager/delete/$', delete_page),
    # url(r'^manager/', ),
    )