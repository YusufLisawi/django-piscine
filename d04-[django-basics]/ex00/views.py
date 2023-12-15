from django.shortcuts import render
from django.http import HttpResponse
import requests
from bs4 import BeautifulSoup

def index(request):
    try:
        res = requests.get('https://www.markdownguide.org/cheat-sheet/')
        res.raise_for_status()
    except requests.HTTPError as e:
        return HttpResponse(e)
    soup = BeautifulSoup(res.text, 'html.parser')
    tables = [str(table) for table in soup.find_all('table')]
    return render(request, 'ex00/index.html', {'tables' : tables})