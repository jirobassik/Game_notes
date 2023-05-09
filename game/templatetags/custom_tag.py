from django import template
from utils.converter_remove import convert_tuple, convert_tuple_price
from utils.init_json_ser_req import genre_json_serializer, genre_request, platform_request, platform_json_serializer, \
    price_request, price_json_serializer

register = template.Library()


@register.simple_tag
def view_genre(list_genre_id: list) -> list:
    dict_id_genres = dict(convert_tuple(genre_json_serializer.decode(genre_request.get_request())))
    return [dict_id_genres.get(id) for id in list_genre_id]


@register.simple_tag
def view_platform(list_platform_id: list) -> list:
    dict_id_platforms = dict(convert_tuple(platform_json_serializer.decode(platform_request.get_request())))
    return [dict_id_platforms.get(id) for id in list_platform_id]


@register.simple_tag
def view_price(game_id: str) -> list:
    price = convert_tuple_price(price_json_serializer.decode(price_request.get_request()))
    return [price_tuple for price_game_id, price_tuple in price if price_game_id == game_id]
