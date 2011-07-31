from django.conf.urls.defaults import patterns, include, url
from pickleback.apps.search import views

urlpatterns = patterns('',
    url(r'^pypi$', 'search.views.pypi', name='pypi'),
)
