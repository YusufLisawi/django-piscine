from django.shortcuts import render
import psycopg2
from django.db import connection 
from django.conf import settings
from django.http import HttpResponse

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
        execute('''CREATE TABLE ex00_movies (
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
