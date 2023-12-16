from django import forms
from django.db import connection

class RemoveForm(forms.Form):
    titles = forms.ChoiceField(choices=[], required=True, widget=forms.Select)

    def __init__(self, *args, **kwargs):
        super(RemoveForm, self).__init__(*args, **kwargs)
        with connection.cursor() as cursor:
            cursor.execute('SELECT title from ex04_movies')
            records = cursor.fetchall()
        self.fields['titles'].choices = [(i[0], i[0]) for i in records]