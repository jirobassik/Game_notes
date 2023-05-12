from django.forms import Form
from django import forms

from utils.converter_remove import find_name
from utils.init_json_ser_req import genre_request, genre_json_serializer

class GameGenreForm(Form):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Название жанра',
    }), label='Название жанра', required=True)

    description = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Описание'
    }), label='Описание', required=False)

    def clean_name(self):
        genre_name = self.cleaned_data['name']
        query_set_games = genre_json_serializer.decode(genre_request.get_request())
        if find_name(query_set_games, genre_name):
            raise forms.ValidationError('Жанр с таким названием уже существует')
        return genre_name
