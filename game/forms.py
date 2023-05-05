from django.forms import Form
from django import forms
from genre.models import GameGenreModel
from genre.serializers import GenreSerializer
from game_platform.models import GamePlatformModel
from game_platform.serializers import GamePlatformSerializer

from utils.tuple_converter import convert_tuple
from utils.request_server import Request
from utils.json_serializer import JsonSerializer

platform_json_serializer = JsonSerializer(GamePlatformModel, GamePlatformSerializer)
genre_json_serializer = JsonSerializer(GameGenreModel, GenreSerializer)
platform_request = Request.platform_model()
genre_request = Request.genre_model()


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
