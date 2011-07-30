from django import forms
from django.forms.widgets import CheckboxSelectMultiple

from pickleback.apps.packages.models import Package

class PackageForm(forms.Form):
    """
    Basic build form
    """
    packages = forms.ModelMultipleChoiceField(
        queryset=Package.objects.all(),
        widget=CheckboxSelectMultiple()
        )

