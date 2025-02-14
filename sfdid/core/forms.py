from django import forms

class MarvelForm(forms.Form):
    name = forms.CharField()
    last_name =forms.CharField()