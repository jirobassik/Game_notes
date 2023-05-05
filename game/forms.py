# from django.forms import ModelForm
# from django import forms
# from game.models import GameModel
#
#
# class GameForm(ModelForm):
#     buy = forms.BooleanField(required=False)
#     beta = forms.BooleanField(required=False)
#     passed = forms.BooleanField(required=False)
#
#     class Meta:
#         model = GameModel
#         fields = ['name', 'description', 'publisher', 'developer', 'genres', 'game_platform', 'buy', 'beta', 'passed', ]
#
#         widgets = {"name": forms.TextInput(attrs={
#             'class': 'form-control',
#             'placeholder': 'Название игры'
#         }), "description": forms.TextInput(attrs={
#             'class': 'form-control',
#             'placeholder': 'Описание'
#         }),
#             "publisher": forms.TextInput(attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Издатель'
#             }), "developer": forms.TextInput(attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Разработчик'
#             }), 'genres': forms.CheckboxSelectMultiple(attrs={
#                 'required': False,
#                 'placeholder': 'Жанры'
#             }),
#             'game_platform': forms.CheckboxSelectMultiple(attrs={
#                 'required': False,
#                 'placeholder': 'Платформы'
#             })}
