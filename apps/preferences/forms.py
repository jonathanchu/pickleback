from django import forms

class PreferenceForm(forms.Form):
    name = forms.CharField(label="Project Name", required=True)
