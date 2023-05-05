from django.forms import Form
from django import forms


class GameGenreForm(Form):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Название жанра',
    }), label='Название жанра', required=True)

    description = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Описание'
    }), label='Описание', required=False)
