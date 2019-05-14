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
    trailer = models.TextField()
    trailer_img = models.TextField()

    @classmethod
    def add_us(cls):
        with open('movies/fixtures/us.csv', 'r') as f:
            fieldnames = ['country', 'rank', 'title', 'year', 'rated', 'released', 'runtime', 'genre', 'director',
                  'actors', 'plot', 'poster', 'imdbID', 'production', 'trailer', 'trailer_img']
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                temp = {key: row[idx] for idx, key in enumerate(fieldnames)}
                Movie.objects.create(**temp)

    def __str__(self):
        return f'{self.country} {self.rank} {self.title}'