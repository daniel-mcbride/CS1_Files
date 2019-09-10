#**********************  turtles.py  *********************
#
# Name: Daniel McBride
#
# Course: CSCI 1470
#
# Assignment: Homework #2
#
# Algorithm:
#   import turtle
#   Create Window and turtle
#   Set position of Pentagon, and start fill
#   Loop through creating pentagon sides and end fill
#   Set position of Hexagon, and start fill
#   Loop through creating hexagon sides and end fill
#   Set position of Octagon, and start fill
#   Loop through creating octagon sides and end fill
#   Set position of Star, and start fill
#   Loop through creating star sides and end fill
#   Set program to end when window closes
#**********************************************************

import turtle

window = turtle.Screen()
bepo = turtle.Turtle()

######## Pentagon ########
# Set location for Pentagon
bepo.penup()
bepo.setpos(-300, 100)
bepo.pendown()

# Prepare fill for Pentagon
bepo.fillcolor("red")
bepo.begin_fill()

# Draw the Pentagon
for i in range(5):
    bepo.forward(100)
    bepo.left(72)

# Stop filling color       
bepo.end_fill()
###### End Pentagon ######


######## Hexagon #########
# Set location for Hexagon
bepo.penup()
bepo.setpos(200, 100)
bepo.pendown()

# Prepare fill for Hexagon
bepo.fillcolor("yellow")
bepo.begin_fill()

# Draw the Hexagon
for i in range(6):
    bepo.forward(75)
    bepo.left(60)

# Stop filling color       
bepo.end_fill()
###### End Hexagon #######


######## Octagon #########
# Set location for Octagon
bepo.penup()
bepo.setpos(-300, -300)
bepo.pendown()

# Prepare fill for Octagon
bepo.fillcolor("blue")
bepo.begin_fill()

# Draw the Octagon
for i in range(8):
    bepo.forward(60)
    bepo.left(45)

# Stop filling color       
bepo.end_fill()
###### End Octagon #######


########## Star ##########
# Set location for Star
bepo.penup()
bepo.setpos(175, -200)
bepo.pendown()

# Prepare fill for Star
bepo.fillcolor("green")
bepo.begin_fill()

# Draw the Star
for i in range(5):
    bepo.forward(125)
    bepo.right(144)

# Stop filling color       
bepo.end_fill()
######## End Star ########

window.mainloop()
