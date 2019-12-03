#**********************  Homework8.py  *********************
#
# Name: Daniel McBride
#
# Course: CSCI 1470
#
# Assignment: Homework #8
#
# Algorithm:
#   Start
#   import turtle
#   import random
#   define winchecker funtion that takes x and y coordinates for both treasure and player
#       if treasure x equals player x
#           set x win to true
#       else if treasure x is greater then player x
#           if treasure x - player x is smaller than the size of the treasure
#               set x win to true
#           else
#               set x win to false
#       else if treasure x is less than player x
#           if player x - treasure x is smaller then the size of the treasure
#               set x win to true
#           else
#               set x win to false
#       check if treasure y equals player y
#           set y win to true
#       else if treasure y is greater then player y
#           if treasure y - player y is smaller than the size of the treasure
#               set y win to true
#           else
#               set y win to false
#       else if treasure y is less than player y
#           if player y - treasure y is smaller then the size of the treasure
#               set y win to true
#           else
#               set y win to false
#       if both x win and y win are true
#           function returns true
#       else
#           function returns false
#   endfunction
#
#   define turn function that takes a direction and degree
#       if the direction is "left
#           call fuction to turn turtle left and supply degree as the argument
#       else if the direction is "right"
#           call fuction to turn turtle right and supply degree as the argument
#   endfunction
#
#   define move funtion that takes a direction and distance
#       if the direction is "forward"
#           for as many times as distance
#               call funtion to move turtle forward by 1
#               set player x to current turtle x value
#               set player y to current turtle y value
#               if checkWin funtion returns true with current player and treasure coordinates
#                   break loop
#           endfor
#       if the direction is "backward"
#           for as many times as distance
#               call funtion to move turtle backward by 1
#               set player x to current turtle x value
#               set player y to current turtle y value
#               if checkWin funtion returns true with current player and treasure coordinates
#                   break loop
#           endfor
#   endfunction
#
#   set window value for turtle screen
#   set turtle to move
#   call penup so no lines are drawn
#   set treasure x to random integer
#   set treasure y to random integer
#   set turtle shape to square
#   set turtle shape to gold
#   send turtle to treasure coordinates
#   stamp turtle
#   set player x to random integer
#   set player y to random integer
#   set turtle shape to classic
#   set turtle color to black
#   send turtle to player coordinates
#   set treasure value to checkWin accepting current player and treasure coordinates
#   while treasure is true
#       prompt player to choose either to turn or move
#       if player entered "turn"
#           prompt player for a direction
#           prompt player for degrees
#           call turn function with direction and degrees provided
#       if player entered "move"
#           prompt player for a direction
#           prompt player for distance
#           call turn function with direction and distance provided
#       set player x value to current turtle x
#       set player y value to current turtle y value
#       set treasure value to the result of checkWin with current player and treasure coordinates
#       if treasure is true
#           show celeblration image
#   endwhile
#   Stop
#**********************************************************

import turtle
import random

#I'll be using this function a lot to see if the player has won
def checkWin(xTreasure, yTreasure, xPlayer, yPlayer):
    #First have to check if the x value is inside the treasure square
    if xTreasure == xPlayer:
        xWin = True
    elif xTreasure > xPlayer:
        if xTreasure - xPlayer <= 10:
            xWin = True
        else:
            xWin = False
    elif xTreasure < xPlayer:
        if xPlayer - xTreasure <= 10:
            xWin = True
        else:
            xWin = False
    #Now have to check if the y value is inside the treasure square            
    if yTreasure == yPlayer:
        yWin = True
    elif yTreasure > yPlayer:
        if yTreasure - yPlayer <= 10:
            yWin = True
        else:
            yWin = False
    elif yTreasure < yPlayer:
        if yPlayer - yTreasure <= 10:
            yWin = True
        else:
            yWin = False
#Only if both are in the square does the player win
    if xWin and yWin:
        return True
    else:
        return False

#This function is how the player will turn themselves    
def turn(direction, degree):
    #All this function does turn based on player input
    if direction == "left" or direction == "l":
        roger.left(degree)
    elif direction == "right" or direction == "r":
        roger.right(degree)
    else:
        return "error"

#This function allows the player to move themselves
def move(direction, distance):
    if direction == "forward" or direction == "f":
        for pixel in range(distance):
            #Only moving the player 1 pixel at a time to checkWin at every point
            roger.forward(1)
            playerX = roger.xcor()
            playerY = roger.ycor()
            if checkWin(treasureX, treasureY, playerX, playerY):
                break
    elif direction == "backward" or direction == "back" or direction == "b":
        for pixel in range(distance):
            #Only moving the player 1 pixel at a time to checkWin at every point
            roger.backward(1)
            playerX = roger.xcor()
            playerY = roger.ycor()
            if checkWin(treasureX, treasureY, playerX, playerY):
                break


input("Welcome to the treasure hunt! Let's start by hitting enter to check our map! ")
wn = turtle.Screen()
roger = turtle.Turtle()
roger.penup()

treasureX = random.randint(-350, 350)
treasureY = random.randint(-300, 300)

roger.shape("square")
roger.color("gold")
roger.goto(treasureX, treasureY)
roger.stamp()

playerX = random.randint(-350, 350)
playerY = random.randint(-300, 300)

roger.shape("classic")
roger.color("black")
roger.goto(playerX, playerY)

treasure = checkWin(treasureX, treasureY, playerX, playerY)

#In case of the player starting on the treasure, the treasure will be moved
while treasure:
    playerX = random.randint(-350, 350)
    playerY = random.randint(-300, 300)
    treasure = checkWin(treasureX, treasureY, playerX, playerY)
    
while not treasure:
    action = input("Do you want to turn or move? ")
    if action == "turn" or action == "t":
        direction = input("Are we turning 'right' or 'left'? ")
        degree = int(input("How many degrees are we turning? "))
        turn(direction, degree)
    elif action == "move" or action == "m":
        direction = input("Are we going 'forward' or 'backward'? ")
        distance = int(input("How far are we going?(In pixels): "))
        move(direction, distance)
    playerX = roger.xcor()
    playerY = roger.ycor()
    treasure = checkWin(treasureX, treasureY, playerX, playerY)
    if treasure:
        wn.clear()
        wn.bgpic("treasure.gif")
        wn.update()
