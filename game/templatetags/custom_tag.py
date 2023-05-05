from django import template
from utils.json_serializer import JsonSerializer
from utils.request_server import Request
from utils.tuple_converter import convert_tuple
from genre.models import GameGenreModel
from genre.serializers import GenreSerializer
from game_platform.models import GamePlatformModel
from game_platform.serializers import GamePlatformSerializer

register = template.Library()
genre_json_serializer = JsonSerializer(GameGenreModel, GenreSerializer)
genre_request = Request.genre_model()
platform_json_serializer = JsonSerializer(GamePlatformModel, GamePlatformSerializer)
platform_request = Request.platform_model()

@register.simple_tag
def view_genre(list_genre_id: list):
    dict_id_genres = dict(convert_tuple(genre_json_serializer.decode(genre_request.get_request())))
    return [dict_id_genres.get(id) for id in list_genre_id]


@register.simple_tag
def view_platform(list_platform_id: list) -> str:
    dict_id_platforms = dict(convert_tuple(platform_json_serializer.decode(platform_request.get_request())))
    return [dict_id_platforms.get(id) for id in list_platform_id]
