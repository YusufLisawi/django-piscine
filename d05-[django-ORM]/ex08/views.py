from django.shortcuts import render
import psycopg2
from django.db import connection 
from django.conf import settings
from django.http import HttpResponse

# Create your views here.

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
            cursor.execute('commit')
    except Exception as e:
        raise e

# Create your views here.
def init(request):
    message = 'OK'
    try:    
        execute('''CREATE TABLE ex08_planets (
    id SERIAL PRIMARY KEY,
    name VARCHAR(64) UNIQUE NOT NULL,
    climate VARCHAR(64),
    diameter INT,
    orbital_period INT,
    population BIGINT,
    rotation_period INT,
    surface_water REAL,
    terrain VARCHAR(128)
);''')

        execute('''CREATE TABLE ex08_people (
    id SERIAL PRIMARY KEY,
    name VARCHAR(64) UNIQUE NOT NULL,
    birth_year VARCHAR(32),
    gender VARCHAR(32),
    eye_color VARCHAR(32),
    hair_color VARCHAR(32),
    height INT,
    mass REAL,
    homeworld VARCHAR(64),
    FOREIGN KEY (homeworld) REFERENCES ex08_planets(name)
);''')
    except Exception as e:
        message =  f'Error: {e}'
    return HttpResponse(message)

def populate(request):
    message = ''
    try:
        with connection.cursor() as cursor:
            with open('./assets/planets.csv') as f:
                cursor.copy_from(f, 'ex08_planets', sep='\t', null='NULL', columns=['name', 'climate', 'diameter', 'orbital_period', 'population', 'rotation_period', 'surface_water', 'terrain'])
                message += f'planets.csv OK<br/>'
            with open('./assets/people.csv') as f:
                cursor.copy_from(f, 'ex08_people', sep='\t', null='NULL', columns=['name', 'birth_year', 'gender', 'eye_color', 'hair_color', 'height', 'mass', 'homeworld'])
                message += f'people.csv OK<br/>'
    except Exception as e:
        message =  f'Error: {e}'
    return HttpResponse(message)

def display(request):
    context = {'people' : [], 'headers' : ['Person Name', 'Planet Name', 'Climate']}
    try:
        with connection.cursor() as cursor:
            cursor.execute(f"""SELECT pe.name, pl.name, pl.climate 
                           FROM ex08_people AS pe 
                           JOIN ex08_planets AS pl
                           ON pe.homeworld = pl.name
                           WHERE pl.climate LIKE '%windy%'
                           ORDER BY pe.name ASC;""")
            records = cursor.fetchall()
        if len(records) == 0:
            raise Exception()
        context['people'] = records
    except Exception as e:
        print(e)
        context['people'] = []
    return render(request, 'ex08/display.html', context)
