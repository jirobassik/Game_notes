from django.forms import Form
from django import forms
from utils.init_json_ser_req import platform_json_serializer, platform_request
from utils.converter_remove import find_name


class GamePlatformForm(Form):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Название платформы',
    }), label='Название платформы', required=True)

    description = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Описание'
    }), label='Описание', required=False)

    def clean_name(self):
        platform_name = self.cleaned_data['name']
        query_set_games = platform_json_serializer.decode(platform_request.get_request())
        if find_name(query_set_games, platform_name):
            raise forms.ValidationError('Платформа с таким названием уже существует')
        return platform_name
