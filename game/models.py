class GameModel:
    def __init__(self, name, description=None, buy=None, beta=None, passed=None, publisher=None, developer=None,
                 genres=None, game_platform=None):
        self.name = name
        self.description = description
        self.buy = buy
        self.beta = beta
        self.passed = passed
        self.publisher = publisher
        self.developer = developer
        self.genres = genres
        self.game_platform = game_platform
