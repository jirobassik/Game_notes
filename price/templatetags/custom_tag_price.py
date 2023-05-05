from django import template
from utils.json_serializer import JsonSerializer
from utils.request_server import Request
from game.models import GameModel
from game.serializers import GameSerializer

register = template.Library()
game_json_serializer = JsonSerializer(GameModel, GameSerializer)
game_request = Request.game_model()


@register.simple_tag
def view_games(game_id: int):
    dict_id_genres = game_json_serializer.detail_decode(game_request.detail_get_request(game_id))
    return dict_id_genres.get('name')

