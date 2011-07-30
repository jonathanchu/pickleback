from django.conf.urls.defaults import patterns, include, url

from pickleback.apps.packages import views

urlpatterns = patterns('',
    # build project
    url(r'^$', 'packages.views.build', name='build'),
)
