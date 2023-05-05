from django.forms import ModelForm
from django import forms
from djmoney.forms import MoneyWidget
from price.models import GamePriceModel


class PriceForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['game'].empty_label = "Игра не выбрана"

    class Meta:
        model = GamePriceModel
        fields = ['name', 'price', 'game']

        widgets = {"name": forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Название магазина'
        }), "game": forms.Select(attrs={
            'class': 'form-select',
            'placeholder': 'Название игры'
        }),
        }
