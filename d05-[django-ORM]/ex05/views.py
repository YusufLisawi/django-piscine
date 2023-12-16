from django.shortcuts import render
from django.http import HttpResponse
from .models import Movies
from .forms import RemoveForm

movies = [
        {
            'episode_nb': 1,
            'title': 'The Phantom Menace',
            'director': 'George Lucas',
            'producer': 'Rick McCallum',
            'release_date': '1999-05-19'
        },
        {
            'episode_nb': 2,
            'title': 'Attack of the Clones',
            'director': 'George Lucas',
            'producer': 'Rick McCallum',
            'release_date': '2002-05-16'
        },
        {
            'episode_nb': 3,
            'title': 'Revenge of the Sith',
            'director': 'George Lucas',
            'producer': 'Rick McCallum',
            'release_date': '2005-05-19'
        },
        {
            'episode_nb': 4,
            'title': 'A New Hope',
            'director': 'George Lucas',
            'producer': 'Gary Kurtz, Rick McCallum',
            'release_date': '1977-05-25'
        },
        {
            'episode_nb': 5,
            'title': 'The Empire Strikes Back',
            'director': 'Irvin Kershner',
            'producer': 'Gary Kurtz, Rick McCallum',
            'release_date': '1980-05-17'
        }
    ]

def populate(request):
    message = ''
    try:
        for movie in movies:
            movie_obj = Movies(
                episode_nb=movie['episode_nb'],
                title=movie['title'],
                director=movie['director'],
                producer=movie['producer'],
                release_date=movie['release_date']
            )
            movie_obj.save()
            message += f'episode_nb: {movie_obj.episode_nb} OK<br/>'
    except Exception as e:
        message = f'Error: {e}'
    return HttpResponse(message)

def display(request):
    context = {'movies' : [], 'headers' : ['title', 'episode_nb', 'opening_crawl', 'director', 'producer', 'release_date ']}
    try:
        records = Movies.objects.all()
        if len(records) == 0:
            raise Exception()
        context['movies'] = records
    except:
        context['movies'] = []
    return render(request, 'display4.html', context)

def remove(request):
    if request.method == 'POST':
        form = RemoveForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['titles']
            try:
                movie = Movies.objects.get(title=title)
                movie.delete()
            except Movies.DoesNotExist:
                return HttpResponse(f'No movie with title {title} found.')
            except Exception as e:
                return HttpResponse(e)
    return render(request, 'form2.html', {'form' : RemoveForm()})