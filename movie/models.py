from django.db import models

# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=30)
    code = models.CharField(max_length=30)

    def __str__(self):
        return f'Country: {self.name}, Country Code: {self.code}'


class Genre(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return f'Genre: {self.name}'


class Score(models.Model):
    score = models.IntegerField()


class Movie(models.Model):
    imdbID = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    rated = models.CharField(max_length=20)
    released = models.DateField()
    runtime = models.IntegerField()
    Genre = models.ManyToManyField(Genre, related_name='genre_movies')
    actors = models.TextField()
    plot = models.TextField()
    poster = models.TextField()
    country = models.OneToOneField(Country, on_delete=models.CASCADE)
    rating = models.TextField()
    imdbscore = models.DecimalField(max_digits=2, decimal_places=1)
    score = models.ForeignKey(Score, related_name='score_movie', on_delete=models.CASCADE)
    production = models.CharField(max_length=30)

    def __str__(self):
        return f'title: {self.title}, released: {self.released}'