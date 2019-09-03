import turtle

backgroundColor = input("What color should the background be? ")
turtleColor = input("How about the color of the turtle? ")
penSize = input("How thick should the line be 1-10? ")
penSize = int(penSize)
penColor = input("What color should the line be? ")

wn = turtle.Screen()
wn.bgcolor(backgroundColor)
wn.title("Hey there, Alita!")

alita = turtle.Turtle()
alita.color(turtleColor)
alita.pensize(penSize)
alita.pencolor(penColor)

alita.forward(50)
alita.left(120)

alita.penup()
alita.forward(50)
alita.pendown()
alita.backward(200)

wn.mainloop()
