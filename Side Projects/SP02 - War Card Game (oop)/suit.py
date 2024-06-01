class Suit:

    SYMBOLS = {
        "clubs" : "♣",
        "diamonds" : "♦",
        "hearts" : "♥",
        "spades" : "♠"
    }
    
    def __init__(self, description):
        self._description = description.lower()
        self._symbol = Suit.SYMBOLS[description.lower()]

    @property
    def description(self):
        return self._description

    @property
    def symbol(self):
        return self._symbol
        