class Card:
    
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
        self.description = value.capitalize() + " of " + suit.capitalize()

    def __str__(self):
        return self.description
    
    def battleValue(self):
        battleValues = {
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9,
            "10": 10,
            "jack": 11,
            "queen": 12,
            "king": 13,
            "ace": 14
        }
        
        return battleValues[self.value]

class Deck:
    
    def __init__(self, cards=None):

        suits = ["spades", "hearts", "clubs", "diamonds"]
        values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "jack", "queen", "king", "ace"]

        if cards is None:
            self.cards = []
            for suit in suits:
                for value in values:
                    self.addToBottom(Card(suit, value))
        else:
            self.cards = cards

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

    def addToBottom(self, card):
        self.cards.append(card)

    def addToTop(self, card):
        self.cards.insert(0, card)
