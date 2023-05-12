from django.forms import Form
from django import forms

from utils.converter_remove import convert_tuple
from utils.init_json_ser_req import platform_json_serializer, genre_request, genre_json_serializer, platform_request, \
    game_request, game_json_serializer
from utils.converter_remove import find_name

class GameForm(Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['genres'] = forms.MultipleChoiceField(
            choices=convert_tuple(genre_json_serializer.decode(genre_request.get_request())),
            widget=forms.CheckboxSelectMultiple(attrs={
                'required': False,
                'placeholder': 'Жанры'}), label='Жанры', required=False)

        self.fields['game_platform'] = forms.MultipleChoiceField(
            choices=convert_tuple(platform_json_serializer.decode(platform_request.get_request())),
            widget=forms.CheckboxSelectMultiple(attrs={
                'required': False,
                'placeholder': 'Платформы'}), label='Платформы', required=False)

    name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Название игры',
    }), label='Название игры', required=True)

    description = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Описание'
    }), label='Описание', required=False)

    publisher = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Издатель'
    }), label='Издатель', required=False)

    developer = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Разработчик'}), label='Разработчик', required=False)

    genres = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple(attrs={
            'required': False,
            'placeholder': 'Жанры'}), label='Жанры', required=False)

    game_platform = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple(attrs={
        'required': False,
        'placeholder': 'Платформы'}), label='Платформы', required=False)

    buy = forms.BooleanField(required=False, label='Куплена')
    beta = forms.BooleanField(required=False, label='Бета')
    passed = forms.BooleanField(required=False, label='Пройдена')

    def clean_name(self):
        name = self.cleaned_data['name']
        query_set_games = game_json_serializer.decode(game_request.get_request())
        if find_name(query_set_games, name):
            raise forms.ValidationError('Игра с таким названием уже существует')
        return name
