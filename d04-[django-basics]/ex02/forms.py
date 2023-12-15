from django import forms

class MyForm(forms.Form):
    field = forms.CharField(max_length=100)
