from django.shortcuts import render, get_list_or_404, get_object_or_404

from .models import Movie, TVSeries
from .forms import MovieCreationForm

import requests
from bs4 import BeautifulSoup
import json

countries = {'us': ['us', 'United States', 'https://cdn.countryflags.com/thumbs/united-states-of-america/flag-800.png'],
             'uk': ['uk', 'United Kingdom', 'https://cdn.countryflags.com/thumbs/united-kingdom/flag-800.png'],
             'fr': ['fr', 'France', 'https://cdn.countryflags.com/thumbs/france/flag-800.png'],
             'au': ['au', 'Australia', 'https://cdn.countryflags.com/thumbs/australia/flag-800.png'],
             'br': ['br', 'Brazil', 'https://cdn.countryflags.com/thumbs/brazil/flag-800.png'],
             'mx': ['mx', 'Mexico', 'https://cdn.countryflags.com/thumbs/mexico/flag-800.png'],}

# Create your views here.
def index(request):
    return render(request, 'movies/index.html')


def country_list(request):
    context = {
        'countries': countries
    }
    return render(request, 'movies/country_list.html', context)


def country_boxoffice(request, country):
    movies = get_list_or_404(Movie, country=country)
    context = {
        'country': country,
        'flag': countries[country][2],
        'country_name': countries[country][1],
        'movies': movies,
    }
    return render(request, 'movies/country_boxoffice.html', context)

def country_detail(request, country, rank):
    movie = get_object_or_404(Movie, country=country, rank=rank)
    context = {
        'country': country,
        'country_name': countries[country][1],
        'movie': movie,
        'directors': movie.director.split(', '),
        'actors': movie.actors.split(', '),
        'genres': movie.genre.split(', '),
    }
    return render(request, 'movies/movie_detail.html', context)

def netflix_list(request):
    serieses = TVSeries.objects.all()
    context = {
        'serieses': serieses
    } 
    return render(request, 'movies/netflix_list.html', context)

def netflix_detail(request, rank):
    series = get_object_or_404(TVSeries, rank=rank)
    context = {
        'series': series,
        'actors': series.actors.split(',\xa0')
    }
    return render(request, 'movies/netflix_detail.html', context)