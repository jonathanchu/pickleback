from django import forms

from pickleback.apps.preferences.models import Preference

class PreferenceForm(forms.ModelForm):
    """
    Preference form
    """
    class Meta:
        model = Preference
