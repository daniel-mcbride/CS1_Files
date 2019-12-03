from deckOfCards import Card
from deckOfCards import Deck

# Need this to store information about the player. Name and deck contents at least.
class Player:
    def __init__(self, name, deck=Deck([])):
        self.name = name
        self.deck = deck

#Runs startup processes that need to run at the beginning of the game
def startGame():
    sourceDeck = Deck()

    sourceDeck.shuffleDeck()
    dealTo = 1
    player1_cards = []
    player2_cards = []
    
    for cardIndex in range(0, len(sourceDeck.cards)):
        if dealTo == 1:
            nextCard = sourceDeck.drawCard()
            player1_cards.append(nextCard)
            dealTo = 2
        elif dealTo == 2:
            nextCard = sourceDeck.drawCard()
            player2_cards.append(nextCard)
            dealTo = 1

    player1_deck = Deck(cards=player1_cards)
    player1Name = input("What is the name of the first player? ")
    player1 = Player(player1Name, deck=player1_deck)

    player2_deck = Deck(cards=player2_cards)
    player2Name = input("What is the name of the second player? ")
    player2 = Player(player2Name, deck=player2_deck)

    print()
    print("Turn 1:")

    players = (player1, player2)
    return players

#Called when one player runs out of cards. Declares the winner, cleans up and prompts for another game, returned as a boolean.
def endGame(winner):
    print("Congratulations, ", winner, "!\nYou have worn down your opponent and claimed victory!", sep="")


#Calls all the other functions needed to play a game
def battle(DEBUG=False, AUTO_WIN=False):
    (player1, player2) = startGame()

    if AUTO_WIN:
        endGame(player1.name)
        quit()

    if DEBUG:
        print("Player 1's Deck:")
        for card in player1.deck.cards:
            print(card)
        print()
        
        print("Player 2's Deck:")
        for card in player2.deck.cards:
            print(card)
        print()

    activePlayer = player1

    pile = []
    card1 = None
    card2 = None
    war = False

    roundCount = 1

    while len(activePlayer.deck.cards) > 0:
        
        if DEBUG:
            print(player1.name, ": ", len(player1.deck.cards), "cards")
            print(player2.name, ": ", len(player2.deck.cards), "cards")
            print("Card 1:", card1)
            print("Card 2:", card2)
            print(pile)

        if war:
            input(activePlayer.name + ", hit enter to add a face down card to the pile")
            pile.append(activePlayer.deck.drawCard())

        if len(activePlayer.deck.cards) > 0:
            input(activePlayer.name + ", hit enter to draw and play your card.")
        else:
            if activePlayer.name == player1.name:
                endGame(player2.name)
                break
            else:
                endGame(player1.name)
                break

        if activePlayer == player1:
            
            if DEBUG:
                print("Player 1 is active")
            
            card1 = activePlayer.deck.drawCard()
            print(card1)
            player1 = activePlayer
            activePlayer = player2
        elif activePlayer == player2:

            if DEBUG:
                print("Player 2 is active")
                
            card2 = activePlayer.deck.drawCard()
            print(card2)
            player2 = activePlayer
            activePlayer = player1
        

        if( card1 != None and card2 != None):
            pile.append(card1)
            pile.append(card2)

            if card1.battleValue() > card2.battleValue():
                print(player1.name, "wins the round! The", len(pile), "cards in play are added to the bottom of their deck!")
                for card in pile:
                    player1.deck.addToBottom(card)

                roundCount += 1

                print()
                print("Current Standings:")
                print(player1.name, ": ", len(player1.deck.cards), "cards")
                print(player2.name, ": ", len(player2.deck.cards), "cards")
                print()
                print("Turn ", roundCount, ":", sep="")
                
                war = False
                pile = []
                activePlayer = player1
            elif card1.battleValue() < card2.battleValue():
                print(player2.name, "wins the round! The", len(pile), "cards in play are added to the bottom of their deck!")
                for card in pile:
                    player2.deck.addToBottom(card)

                roundCount += 1

                print()
                print("Current Standings:")
                print(player1.name, ": ", len(player1.deck.cards), "cards")
                print(player2.name, ": ", len(player2.deck.cards), "cards")
                print()
                print("Round ", roundCount, ":", sep="")
                
                war = False
                pile = []
                activePlayer = player2
            elif card1.battleValue() == card2.battleValue():
                print("It's a tie! Time to settle it with another battle!")
                war = True

            card1 = None
            card2 = None









