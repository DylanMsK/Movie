from django.db import models

# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=30)
    code = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Score(models.Model):
    score = models.IntegerField()


class Movie(models.Model):
    imdbID = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    rated = models.CharField(max_length=20, null=True, blank=True)
    released = models.DateField()
    runtime = models.IntegerField()
    Genre = models.ManyToManyField(Genre, related_name='genre_movies')
    actors = models.TextField()
    plot = models.TextField()
    poster = models.TextField()
    country = models.OneToOneField(Country, on_delete=models.CASCADE)
    rating = models.TextField()
    imdbscore = models.DecimalField(max_digits=2, decimal_places=1, null=True, blank=True)
    score = models.ForeignKey(Score, related_name='score_movie', on_delete=models.CASCADE, null=True, blank=True)
    production = models.CharField(max_length=30)

    def __str__(self):
        return f'title: {self.title}, released: {self.released}'


class BoxOffice(models.Model):
    year = models.IntegerField()
    weak = models.IntegerField()
    rank = models.IntegerField()
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self):
        return f'[{self.country}] {self.year}년/{self.weak}주차 {self.rank}위 {self.movie}'
