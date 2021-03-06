from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import Movie, TVSeries


# Register your models here.
class MovieAdmin(ImportExportModelAdmin):
    list_per_page = 20
    list_display = ('id', 'country', 'rank', 'title', 'genre', 'released', )
    list_filter = ('country', 'rank', )
    search_fields = ('genre',)
    ordering = ('id', 'rank',)


class TVSeriesAdmin(ImportExportModelAdmin):
    list_per_page = 20
    list_display = ('id', 'rank', 'title', 'season',)
    search_fields = ('title', 'genre',)


admin.site.register(Movie, MovieAdmin)
admin.site.register(TVSeries, TVSeriesAdmin)