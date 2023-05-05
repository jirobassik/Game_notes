class GamePriceModel:
    def __init__(self, name, price, game, price_currency):
        self.price_currency = price_currency
        self.game = game
        self.price = price
        self.name = name
