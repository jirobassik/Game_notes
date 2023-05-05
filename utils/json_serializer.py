from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from io import BytesIO

class JsonSerializer:
    def __init__(self, model, model_serializer):
        self.model = model
        self.model_serializer = model_serializer

    def encode(self, **kwargs):
        model = self.model(**kwargs)
        model_sr = self.model_serializer(model)
        return JSONRenderer().render(model_sr.data)

    def decode(self, raw_data):
        stream = BytesIO(raw_data)
        data = JSONParser().parse(stream)
        serializer = self.model_serializer(data=data, many=True)
        serializer.is_valid(raise_exception=False)
        return serializer.validated_data

    def detail_decode(self, raw_data):
        stream = BytesIO(raw_data)
        data = JSONParser().parse(stream)
        serializer = self.model_serializer(data=data)
        serializer.is_valid(raise_exception=False)
        return serializer.validated_data
