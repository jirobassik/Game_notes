from rest_framework import serializers
from genre.serializers import GenreSerializer
from game_platform.serializers import GamePlatformSerializer
from django import forms


class GameSerializer(serializers.Serializer):
    # id = serializers.IntegerField(required=True)
    # name = serializers.CharField(max_length=70, allow_null=False, allow_blank=False,
    #                              style={'placeholder': 'Название игры', 'class': 'form-control'})
    # description = serializers.CharField(max_length=255, allow_null=True, allow_blank=True,
    #                                     style={'placeholder': 'Описание', 'class': 'form-control'})
    # buy = serializers.BooleanField(default=False, help_text='Куплена игра или нет', )
    # beta = serializers.BooleanField(default=False, help_text='Игра находится в бета тестировании или нет')
    # passed = serializers.BooleanField(default=False, help_text='Игра пройдена или нет')
    # publisher = serializers.CharField(max_length=70, allow_null=True, allow_blank=True,
    #                                   style={'placeholder': 'Издатель', 'class': 'form-control'})
    # developer = serializers.CharField(max_length=70, allow_null=True, allow_blank=True,
    #                                   style={'placeholder': 'Разработчик', 'class': 'form-control'})
    # genres = serializers.ListField(child=serializers.IntegerField(), required=False,
    #                                style={'placeholder': 'Жанры', 'class': 'form-control'})
    # game_platform = serializers.ListField(child=serializers.IntegerField(), required=False,
    #                                       style={'placeholder': 'Платформы', 'class': 'form-control'})

    id = serializers.IntegerField(required=True)
    name = serializers.CharField(max_length=70, allow_null=False, allow_blank=False,
                                 style={'placeholder': 'Email', 'autofocus': True})
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
    # --
    # genres = GenreSerializer(many=True, read_only=True)
    # game_platform = GamePlatformSerializer(many=True, read_only=True)
    # --
    # genres = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # game_platform = serializers.ListField(child=serializers.PrimaryKeyRelatedField(many=True, read_only=True)


'''    name = models.CharField("Название игры", max_length=70, unique=True, null=False, blank=False, db_index=True)
    description = models.TextField("Описание", max_length=255, null=True, blank=True)
    buy = models.BooleanField("Куплена", default=False, help_text="Куплена игра или нет")
    beta = models.BooleanField("Игра в бете", default=False, help_text="Игра находится в бета тестировании или нет")
    passed = models.BooleanField("Игра пройдена", default=False, help_text="Игра пройдена или нет")
    publisher = models.CharField("Издатель", max_length=70, null=True, blank=True)
    developer = models.CharField("Разработчик", max_length=70, null=True, blank=True)
    genres = models.ManyToManyField(GameGenreModel, blank=True)
    game_platform = models.ManyToManyField(GamePlatformModel, blank=True)'''
