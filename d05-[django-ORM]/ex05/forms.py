from django import forms
from .models import Movies

class RemoveForm(forms.Form):
    titles = forms.ChoiceField(choices=[], required=True)

    def __init__(self, *args, **kwargs):
        super(RemoveForm, self).__init__(*args, **kwargs)
        self.fields['titles'].choices = [(str(i), str(i)) for i in Movies.objects.all()]