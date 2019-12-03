from deckOfCards import Card
from deckOfCards import Deck

# Need this to store information about the player. Name and deck contents at least.
class Player:
    def __init__(self, name, deck=Deck("empty")):
        self.name = name
        self.deck = deck

#Runs startup processes that need to run at the beginning of the game
def startGame():
    sourceDeck = Deck()

    player1Name = input("What is the name of the first player? ")
    player1 = Player(player1Name)

    player2Name = input("What is the name of the second player? ")
    player2 = Player(player2Name)

    sourceDeck.shuffleDeck()
    dealTo = 1
    for card in sourceDeck.cards:
        if dealTo == 1:
            player1.deck.cards.append(sourceDeck.drawCard())
            dealTo = 2
        elif dealTo == 2:
            player1.deck.cards.append(sourceDeck.drawCard())
            dealTo = 1

    players = (player1, player2)
    return players

#Runs through one player's side of a turn, and plays differently if the previous turn was a tie
def playTurn(player, war):
    pass

def checkWinner(card1, card2):
    pass

#Called when one player runs out of cards. Declares the winner, cleans up and prompts for another game, returned as a boolean.
def endGame(winner):
    pass


#Calls all the other functions needed to play a game
def battle():
    (player1, player2) = startGame()

    activePlayer = player1

    pile = []
    var card1 = None
    var card2 = None
    war = False

    while len(activePlayer.deck.cards) > 0:
        playTurn(activePlayer, war)

        if( card1 != None and card2 != None):
            winner = checkWinner(card1, card2)

            if winner == card1





