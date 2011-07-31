from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.core.servers.basehttp import FileWrapper

from pickleback.apps.packages.models import Package
from pickleback.apps.packages.forms import PackageForm
from pickleback.apps.preferences.forms import PreferenceForm
from pickleback.apps.vinegar import build_package
import os 

def build(request):
    """
    List all packages available for build
    """
    packages = Package.objects.all()
    
    if request.method == "POST":
        preference_form = PreferenceForm(request.POST)
        package_form = PackageForm(request.POST)
        if package_form.is_valid() and preference_form.is_valid():
            req_pkg = package_form.cleaned_data['packages']
            req_pkg = [p.canonical for p in packages]
            name = preference_form.cleaned_data['name']
            f = build_package.bundle(name, unicode(req_pkg))
            wrapper = FileWrapper(file(f))
            response = HttpResponse(wrapper, content_type="application/x-gzip")
            response['Content-Length'] = os.path.getsize(f)
            return response
    else:
        package_form = PackageForm()
        preference_form = PreferenceForm()
            
    return render_to_response('packages/packages.html', {
        'packages': packages,
        'package_form': package_form,
        'preference_form': preference_form,
    }, context_instance=RequestContext(request))
