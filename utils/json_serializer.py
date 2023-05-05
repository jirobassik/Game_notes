from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from io import BytesIO

class JsonSerializer:
    def __init__(self, model, model_serializer):
        self.model = model
        self.model_serializer = model_serializer

    def encode(self, **kwargs):
        model = self.model(**kwargs)
        print('model', model)
        model_sr = self.model_serializer(model)
        print('model_sr', model_sr.data, type(model_sr.data), sep='\n')
        json_ = JSONRenderer().render(model_sr.data)
        print('json', json_, type(json_), sep='\n')
        return json_

    def decode(self, raw_data):
        print(raw_data)
        stream = BytesIO(raw_data)
        data = JSONParser().parse(stream)
        print('data', data)
        serializer = self.model_serializer(data=data, many=True)
        print(serializer.is_valid(raise_exception=False))
        print(serializer.errors)
        print('serialize data', serializer.validated_data)
        return serializer.validated_data

    def detail_decode(self, raw_data):
        print(raw_data)
        stream = BytesIO(raw_data)
        data = JSONParser().parse(stream)
        print('data', data)
        serializer = self.model_serializer(data=data)
        print(serializer.is_valid(raise_exception=False))
        print(serializer.errors)
        print('serialize data', serializer.validated_data)
        return serializer.validated_data
