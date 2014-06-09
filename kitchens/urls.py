__author__ = 'sungjin'
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView
from kitchens.views import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'EightFookCourt.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^kitchens', cook_controller),
    url(r'^takefood', take_food),
    url(r'^finishalarm', alarm_to),

    # url(r'^'),
    # url(r'^manager/', ),
    )