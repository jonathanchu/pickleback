from django.shortcuts import render_to_response, redirect
from django.template import RequestContext

from pickleback.apps.packages.models import Package

def build(request):
    """
    List all packages available for build
    """
    packages = Package.objects.all()

    return render_to_response('packages/packages.html', {
        'packages': packages,
    }, context_instance=RequestContext(request))
