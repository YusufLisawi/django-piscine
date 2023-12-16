from django.shortcuts import render
import psycopg2
from django.db import connection 
from django.conf import settings
from django.http import HttpResponse
from .forms import RemoveForm
from django.shortcuts import redirect

# Create your views here.
table_name = 'ex04_movies'
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

def connect_execute(sql: str):
    db = settings.DATABASES.default
    try:
        conn = psycopg2.connect(
            database=db['NAME'],
            user=db['USER'],
            password=db['PASSWORD'],
            host=db['HOST'],
            port=db['PORT'],
        )
        with conn.cursor() as cursor:
            cursor.execute(sql)
            conn.commit()
        conn.close()
    except psycopg2.Error as e:
        conn.close()
        raise e

def execute(sql: str):
    try:
        with connection.cursor() as cursor:
            cursor.execute(sql)
    except Exception as e:
        raise e

# Create your views here.
def init(request):
    message = 'OK'
    try:    
        execute('''CREATE TABLE {table_name} (
            title VARCHAR(64) UNIQUE NOT NULL,
            episode_nb INT PRIMARY KEY,
            opening_crawl TEXT,
            director VARCHAR(32) NOT NULL,
            producer VARCHAR(128) NOT NULL,
            release_date DATE NOT NULL
        );''')
    except Exception as e:
        message =  f'Error: {e}'
    return HttpResponse(message)

def make_insert_values(object: dict) -> str:
    keys = ', '.join([str(k) for k in object.keys()])
    values = tuple([v for v in object.values()])
    return f"({keys}) VALUES {str(values)}"

def populate(request):
    message = ''
    try:
        for movie in movies:
            query = f'INSERT INTO {table_name} {make_insert_values(movie)};'
            print(query)
            execute(query)
            message += f'episode_nb: {movie["episode_nb"]} OK<br/>'
    except Exception as e:
        message =  f'Error: {e}'
    return HttpResponse(message)

def display(request):
    context = {'movies' : [], 'headers' : ['title', 'episode_nb', 'opening_crawl', 'director', 'producer', 'release_date ']}
    try:
        with connection.cursor() as cursor:
            cursor.execute(f'SELECT * FROM {table_name};')
            records = cursor.fetchall()
        if len(records) == 0:
            raise Exception()
        context['movies'] = records
    except:
        context['movies'] = []
    return render(request, 'display3.html', context)

def remove(request):
    if request.method == 'POST':
        form = RemoveForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['titles']
            try:
                execute(f'DELETE FROM {table_name} WHERE title=\'{title}\'')
            except Exception as e:
                return HttpResponse(e)
    return render(request, 'form.html', {'form' : RemoveForm()})