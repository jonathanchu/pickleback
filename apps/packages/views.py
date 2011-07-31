from django.shortcuts import render_to_response, redirect
from django.template import RequestContext

from pickleback.apps.packages.models import Package
from pickleback.apps.packages.forms import PackageForm
from pickleback.apps.preferences.forms import PreferenceForm

def build(request):
    """
    List all packages available for build
    """
    packages = Package.objects.all()

    if request.method == "POST":
        preference_form = PreferenceForm(request.POST)
        package_form = PackageForm(request.POST)
        if package_form.is_valid() and preference_form.is_valid():
            packages = package_form.cleaned_data['packages']
            project_name = preference_form.cleaned_data['name']
            admin = preference_form.cleaned_data['admin']
            database = preference_form.cleaned_data['database']
    else:
        package_form = PackageForm()
            
    return render_to_response('packages/packages.html', {
        'packages': packages,
        'package_form': package_form,
        'preference_form': preference_form,
    }, context_instance=RequestContext(request))
