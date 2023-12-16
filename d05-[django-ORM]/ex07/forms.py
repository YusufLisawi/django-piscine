from django import forms
from .models import Movies

class UpdateForm(forms.Form):
    title = forms.ChoiceField(choices=[], required=True)
    opening_crawl = forms.CharField(label="Opening crawl", widget=forms.Textarea)
    
    def __init__(self, *args, **kwargs):
        super(UpdateForm, self).__init__(*args, **kwargs)
        self.fields['title'].choices = [(str(i), str(i)) for i in Movies.objects.all()]