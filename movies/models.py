from django.db import models
import csv


# Create your models here.
class Movie(models.Model):
    country = models.CharField(max_length=100)
    rank = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    year = models.CharField(max_length=100)
    rated = models.CharField(max_length=100)
    released = models.CharField(max_length=100)
    runtime = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    actors = models.CharField(max_length=100)
    plot = models.TextField()
    poster = models.TextField()
    imdbID = models.CharField(max_length=100)
    production = models.CharField(max_length=100)
    imdbScore = models.CharField(max_length=100)
    trailer = models.TextField()
    trailer_img = models.TextField()

    @classmethod
    def add(cls):
        with open('movies/fixtures/movies.csv', 'r') as f:
            fieldnames = ['country', 'rank', 'title', 'year', 'rated', 'released', 'runtime', 'genre', 'director',
                  'actors', 'plot', 'poster', 'imdbID', 'production', 'imdbScore', 'trailer', 'trailer_img']
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                temp = {key: row[idx] for idx, key in enumerate(fieldnames)}
                Movie.objects.create(**temp)

    def __str__(self):
        return f'{self.country} {self.rank} {self.title}'


class TVSeries(models.Model):
    rank = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    netflix_url = models.TextField()
    year = models.CharField(max_length=100)
    rated = models.CharField(max_length=100)
    season = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    plot = models.TextField()
    actors = models.CharField(max_length=100)
    trailer = models.TextField()
    thumbnail = models.TextField()

    @classmethod
    def add(cls):
        with open('movies/fixtures/netflix.csv', 'r') as f:
            fieldnames = ['rank', 'title', 'netflix_url', 'year', 'rated', 'season', 'genre', 'plot', 'actors',
                        'trailer', 'thumbnail']
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                temp = {key: row[idx] for idx, key in enumerate(fieldnames)}
                TVSeries.objects.create(**temp)

    def __str__(self):
        return self.title