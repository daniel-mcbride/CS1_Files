class Card:
    
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
        self.description = value.capitalize() + " of " + suit.capitalize()

    def __str__(self):
        return self.description
