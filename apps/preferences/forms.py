from django import forms

class PreferenceForm(forms.Form):
    name = forms.CharField(max_length=100, label="Project Name", required=True,
                           widget=forms.TextInput(attrs={"size": 35}))
