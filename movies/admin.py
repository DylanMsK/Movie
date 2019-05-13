from django.contrib import admin
from .models import Country, Genre, Score, Movie, BoxOffice

# Register your models here.
admin.site.register(Country)
admin.site.register(Genre)
admin.site.register(Score)
admin.site.register(Movie)
admin.site.register(BoxOffice)