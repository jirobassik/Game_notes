import requests


class Request:
    def __init__(self, model_name: str):
        self.__model_name = model_name

    @classmethod
    def game_model(cls):
        return cls('games')

    @classmethod
    def genre_model(cls):
        return cls('genre')

    @classmethod
    def platform_model(cls):
        return cls('platform')

    @classmethod
    def price_model(cls):
        return cls('price')

    def get_request(self):
        return requests.get(f'http://127.0.0.1:8001/api/v1/{self.model_name}/').content

    def detail_get_request(self, id):
        return requests.get(f'http://127.0.0.1:8001/api/v1/{self.model_name}/{id}/').content

    def post_request(self, data: dict):
        requests.post(f'http://127.0.0.1:8001/api/v1/{self.model_name}/', data=data,
                      headers={'Content-Type': 'application/json'})

    def put_request(self, data, id):
        requests.put(f'http://127.0.0.1:8001/api/v1/{self.model_name}/{id}/', data=data,
                     headers={'Content-Type': 'application/json'})

    def delete_request(self, id):
        requests.delete(f'http://127.0.0.1:8001/api/v1/{self.model_name}/{id}/')

    @property
    def model_name(self):
        return self.__model_name
