from django.shortcuts import render
from django.http import HttpResponse
from .models import Planets, People

# Create your views here.
def display(request):
    context = {'people' : [], 'headers' : ['Person Name', 'Planet Name', 'Climate']}
    try:
        records = People.objects.filter(homeworld__climate__contains='windy').order_by('name').values_list('name', 'homeworld__name', 'homeworld__climate')
        if len(records) == 0:
            raise Exception()
        context['people'] = list(records)
    except Exception as e:
        print(e)
        context['people'] = []
    return render(request, 'ex09/display.html', context)