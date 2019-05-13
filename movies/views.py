from django.shortcuts import render

from .models import Movie
from .forms import MovieCreationForm
from .serializer import MovieSerializer

from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET'])
def movie_list(request):
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)


# def new_movie(request):
#     if request.method == 'POST':
#         form = MovieCreationForm(request.POST)
#         if form.is_valid():
#             movie = Movie(**form.cleaned_data)
#             movie


def country_box_office(request):
    return


def movie_detail(request):
    return