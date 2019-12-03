#***************  McbrideD_CSCI1470_HW5.py  ***************
#
# Name: Daniel McBride
#
# Course: CSCI 1470
#
# Assignment: Homework #5
#
# Algorithm:
#   Start
#   
#**********************************************************

import random

player1 = 0
player2 = 0

def roll_die():
    return random.randint(1, 6)

def take_turn(currentScore):
    extraTurn = True
    
    newScore = currentScore

    while True:
    
        die1 = roll_die()
        die2 = roll_die()
        die3 = roll_die()

        print("You rolled a ", die1, ", ", die2, " and ", die3, sep="")

        if die1 == 6:
            if die2 == 6:
                if die3 == 6:
                    newScore += 21
                    print("All sixes! Way to go!")
                    return newScore
            elif die3 == 6:
                newScore += 5
            else:
                newScore += 1
        elif die2 == 6:
            if die3 == 6:
                newScore += 5
            else:
                newScore += 1
        elif die3 == 6:
            newScore += 1
        elif die1 == die2 and die2 == die3:
            pass
        else:
            break

        pointChange = newScore - currentScore
        currentScore = newScore

        if pointChange == 0:
            input("All matching, Take an extra roll!")
        if pointChange == 1:
            if newScore < 21:
                input(str(pointChange) + " point! Hit enter to roll again! ")
            else:
                print("1 point!")
                return newScore
        else:
            if newScore < 21:
                input(str(pointChange) + " points! Hit enter to roll again! ")
            else:
                print(pointChange, "points!")
                return newScore

    return newScore

while True:
    input("Player 1, hit enter to take your turn ")
    player1 = take_turn(player1)
    if player1 >= 21:
        print("Player 1 wins!!")
        break
    else:
        print("Player 1's turn is over with a score of", player1, end="\n\n")

    input("Player 2, hit enter to take your turn ")
    player2 = take_turn(player2)
    if player2 >= 21:
        print("Player 2 wins!!")
        break
    else:
        print("Player 2's turn is over with a score of", player2, end="\n\n")
