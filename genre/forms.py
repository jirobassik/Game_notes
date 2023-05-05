from django.forms import ModelForm
from django import forms
from genre.models import GameGenreModel


class GenreForm(ModelForm):

    class Meta:
        model = GameGenreModel
        fields = ['name', 'description', ]
        widgets = {"name": forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Название жанра'
        }), "description": forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Описание жанра'
        }),}
