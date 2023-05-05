from rest_framework import serializers
from django import forms


class GameSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False, write_only=True)
    name = serializers.CharField(max_length=70, allow_null=False, allow_blank=False, label='Название игры',
                                 style={'autofocus': True, 'class': 'form-control', 'placeholder': 'Название игры',
                                        'label': 'Название игры'})
    description = serializers.CharField(max_length=255, allow_null=True, allow_blank=True, )
    buy = serializers.BooleanField(default=False, help_text='Куплена игра или нет', )
    beta = serializers.BooleanField(default=False, help_text='Игра находится в бета тестировании или нет')
    passed = serializers.BooleanField(default=False, help_text='Игра пройдена или нет')
    publisher = serializers.CharField(max_length=70, allow_null=True, allow_blank=True, )
    developer = serializers.CharField(max_length=70, allow_null=True, allow_blank=True, )
    genres = serializers.ListField(child=serializers.IntegerField(), required=False, )
    game_platform = serializers.ListField(child=serializers.IntegerField(), required=False, )

    class Meta:
        fields = ('name', 'description', 'buy', 'beta', 'passed', 'publisher', 'developer', 'genres', 'game_platform')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Название игры'}, ),
            'description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Описание'}),
            'publisher': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Издатель'}),
            'developer': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Разработчик'}),
            'genres': forms.SelectMultiple(attrs={'class': 'form-control', 'placeholder': 'Жанры'}),
            'game_platform': forms.SelectMultiple(attrs={'class': 'form-control', 'placeholder': 'Платформы'}),
        }
        labels = {
            'name': 'Название игры',
            'description': 'Описание',
            'publisher': 'Издатель',
            'developer': 'Разработчик',
            'genres': 'Жанры',
            'game_platform': 'Платформы'
        }
        help_texts = {
            'buy': 'Куплена игра или нет',
            'beta': 'Игра находится в бета тестировании или нет',
            'passed': 'Игра пройдена или нет'
        }

        media = forms.Media(
            css={
                'all': ('game/css/create.css',)
            }
        )
