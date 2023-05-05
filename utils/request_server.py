import io

import requests
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from game.models import GameModel
from game.serializers import GameSerializer


def get_request():
    request_data = requests.get('http://127.0.0.1:8001/api/v1/games/')
    return request_data.content


def delete_request(id):
    requests.delete(f'http://127.0.0.1:8001/api/v1/games/{id}/')


def encode():
    model = GameModel('Angelina Jolie', 'Content: Angelina Jolie')
    model_sr = GameSerializer(model)
    print(model_sr.data, type(model_sr.data), sep='\n')
    json = JSONRenderer().render(model_sr.data)
    print(json, type(json), sep='\n')


def decode():
    raw_data = get_request()
    print(raw_data)
    stream = io.BytesIO(raw_data)
    data = JSONParser().parse(stream)
    print('data', data)
    serializer = GameSerializer(data=data, many=True)
    print(serializer.is_valid(raise_exception=False))
    print(serializer.errors)
    print('serialize data', serializer.validated_data)
    return serializer.validated_data
