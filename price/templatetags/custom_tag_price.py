from django import template
from utils.init_json_ser_req import game_json_serializer, game_request

register = template.Library()


@register.simple_tag
def view_games(game_id: int):
    dict_id_genres = game_json_serializer.decode(game_request.detail_get_request(game_id), many=False)
    return dict_id_genres.get('name')
