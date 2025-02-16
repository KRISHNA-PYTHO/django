from django import forms

class AdmissionForm(forms.Form):
    name = forms.CharField()
    last_name =forms.CharField()