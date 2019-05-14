from django.shortcuts import render

from .models import Movie
from .forms import MovieCreationForm

import requests
from bs4 import BeautifulSoup
import json


# Create your views here.
def us_boxoffice(request):
    movies = Movie.objects.all()
    context = {
        'country_name': 'United State',
        'movies': movies,
    }
    return render(request, 'movies/index.html', context)