from game.models import GameModel
from game.serializers import GameSerializer
from genre.models import GameGenreModel
from genre.serializers import GenreSerializer
from price.serializers import GamePriceSerializer
from price.models import GamePriceModel
from game_platform.serializers import GamePlatformSerializer
from game_platform.models import GamePlatformModel

from utils.request_server import Request
from utils.json_serializer import JsonSerializer

platform_json_serializer = JsonSerializer(GamePlatformModel, GamePlatformSerializer)
platform_request = Request.platform_model()

price_json_serializer = JsonSerializer(GamePriceModel, GamePriceSerializer)
price_request = Request.price_model()

game_json_serializer = JsonSerializer(GameModel, GameSerializer)
game_request = Request.game_model()

genre_request = Request.genre_model()
genre_json_serializer = JsonSerializer(GameGenreModel, GenreSerializer)
