from django.db import models

# Create your models here.
class Movies(models.Model):
    class Meta:
        db_table = "ex05_movies" # To change the table name

    title = models.CharField(unique=True, max_length=64)
    episode_nb = models.IntegerField(primary_key=True)
    opening_crawl = models.TextField(null=True)
    director = models.CharField(max_length=32)
    producer = models.CharField(max_length=128)
    release_date = models.DateField()

    def __str__(self):
        return self.title
    