import Card

class Deck:
    
    def __init__(self):
        suits = ["spades", "hearts", "clubs", "diamonds"]
        values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "jack", "queen", "king", "ace"]

        self.cards = []
        
        for suit in suits:
            for value in values:
                self.cards.append(Card.Card(suit, value))

    def __str__(self):
        printStr = ""
        
        for card in self.cards:
            printStr += card.description + "\n"

        return printStr

    def shuffleDeck(self):
        from random import randint
        
        tempDeck = self.cards
        newDeck = []

        while len(tempDeck) > 0:
            currentCard = randint(0, (len(tempDeck) - 1))
            newDeck.append(tempDeck.pop(currentCard))

        self.cards = newDeck
