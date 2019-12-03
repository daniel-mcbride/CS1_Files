class Card:
    
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
        self.description = value.capitalize() + " of " + suit.capitalize()

    def __str__(self):
        return self.description

class Deck:
    
    def __init__(self, deckType="standard"):

        suits = ["spades", "hearts", "clubs", "diamonds"]
        values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "jack", "queen", "king", "ace"]

        self.cards = []

        if deckType == "standard":
            for suit in suits:
                for value in values:
                    self.cards.append(Card(suit, value))

    def inspectDeck(self):
        for card in self.cards:
            print(card)

    def shuffleDeck(self):
        from random import randint
        
        tempDeck = self.cards
        newDeck = []

        while len(tempDeck) > 0:
            currentCard = randint(0, (len(tempDeck) - 1))
            newDeck.append(tempDeck.pop(currentCard))

        self.cards = newDeck

    def drawCard(self):
        return self.cards.pop(0)
    
