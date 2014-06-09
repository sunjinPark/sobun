from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'EightFookCourt.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('menus.urls')),
    url(r'^', include('stores.urls')),
    url(r'^', include('kitchens.urls')),
    url(r'^', include('users.urls')),
    url(r'^', include('clients.urls')),
)
