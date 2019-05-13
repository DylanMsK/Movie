from django import forms
from .models import Movie

import requests
import json

class MovieCreationForm(forms.ModelForm):
    title = forms.CharField(max_length = 100)
    year = forms.IntegerField()

    def clean(self):
        cleaned_data = super(MovieCreationForm, self).clean()
        title = cleaned_data['title']
        year = cleaned_data['year']
        api_url = f'http://www.omdbapi.com/?apikey=556ed6ed&t={title}&y={year}&plot=full'
        data = json.loads(requests.get(api_url).text)
        if data['Response'] == 'False':
            raise forms.ValidationError('영화가 없다!!!!!!!!!!')

        cleaned_data['imdbId'] = data['imdbID']
        cleaned_data['rated'] = data['Rated']
        cleaned_data['released'] = data['Released']
        cleaned_data['runtime'] = data['Runtime']
        cleaned_data['actors'] = data['Actors']
        cleaned_data['plot'] = data['Plot']
        cleaned_data['poster'] = data['Poster']
        cleaned_data['ratings'] = data['Ratings']
        cleaned_data['imdbRating'] = data['imdbRating']
        cleaned_data['production'] = data['Production']
        return cleaned_data