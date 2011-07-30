from django.shortcuts import render_to_response, redirect
from django.template import RequestContext

from pickleback.apps.packages.models import Package
from pickleback.apps.packages.forms import PackageForm

def build(request):
    """
    List all packages available for build
    """
    packages = Package.objects.all()
    package_form = PackageForm()

    return render_to_response('packages/packages.html', {
        'packages': packages,
        'package_form': package_form,
    }, context_instance=RequestContext(request))
