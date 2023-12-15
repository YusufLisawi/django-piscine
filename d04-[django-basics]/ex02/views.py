from django.shortcuts import render
from django.http import HttpResponse
from . import forms

# Create your views here.
history = []

def index(request):
    global history

    if request.method == 'POST':
        form = forms.MyForm(request.POST)
        if form.is_valid():
            field_value = form.cleaned_data['field']
            history.append(field_value)
    else:
        form = forms.MyForm()
    return render(request, 'ex02/index.html', {'form' : form, 'history' : history})