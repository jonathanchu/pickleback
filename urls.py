from django.conf.urls.defaults import patterns, include, url
from django.views.generic.simple import direct_to_template
from django.contrib import admin
admin.autodiscover()

import settings

urlpatterns = patterns('',
    # home
    url(r'^$', direct_to_template, { "template": "home.html", }, name="home"),

    # django-sentry
    (r'^sentry/', include('sentry.web.urls')),

    # admin
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$',
         'django.views.static.serve',
         {'document_root': settings.MEDIA_ROOT, 'show_indexes': True, }),
        (r'^static/(?P<path>.*)$',
         'django.views.static.serve',
         {'document_root': settings.STATIC_ROOT, 'show_indexes': True, }),
)
