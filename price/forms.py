from django.forms import Form
from django import forms
from game.models import GameModel
from game.serializers import GameSerializer
from utils.json_serializer import JsonSerializer
from utils.request_server import Request
from utils.converter_remove import convert_tuple

game_json_serializer = JsonSerializer(GameModel, GameSerializer)
game_request = Request.game_model()


class PriceForm(Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['game'] = forms.ChoiceField(
            choices=[("", "Игра не выбрана")] + convert_tuple(game_json_serializer.decode(game_request.get_request())),
            widget=forms.Select(attrs={
                'class': 'form-select',
                'placeholder': 'Название игры',
            }), label='Название игры', required=True, initial=None)

        self.fields['game'].empty_label = "Игра не выбрана"

    name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Название магазина',
    }), label='Название магазина', required=True)

    price = forms.DecimalField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Цена', }), label="Цена")

    game = forms.ChoiceField(
        choices=[("", "Игра не выбрана")] + convert_tuple(game_json_serializer.decode(game_request.get_request())),
        widget=forms.Select(attrs={
            'class': 'form-select',
            'placeholder': 'Название игры',
        }), label="Название игры", required=True, initial=None)
