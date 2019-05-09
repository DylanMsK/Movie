from django.contrib import admin
from .models import Country, Genre, Score, Movie

# Register your models here.
admin.site.register(Country)
admin.site.register(Genre)
admin.site.register(Score)
admin.site.register(Movie)