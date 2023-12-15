from django.shortcuts import render
from django.http import HttpResponse
from . import forms
import logging
from django.conf import settings

# Create your views here.
def index(request):
    logger = logging.getLogger('history')

    if request.method == 'POST':
        form = forms.MyForm(request.POST)
        if form.is_valid():
            field_value = form.cleaned_data['field']
            logger.info(field_value)
    else:
        form = forms.MyForm()
    try:
        print(settings.HISTORY_LOG_FILE)
        with open(settings.HISTORY_LOG_FILE, 'r') as f:
            history = [line for line in f.readlines()]
    except:
        history = []
    return render(request, 'ex02/index.html', {'form' : form, 'history' : history})