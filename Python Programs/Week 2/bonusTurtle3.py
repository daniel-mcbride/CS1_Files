import turtle
scrn1 = turtle.Screen()
scrn1.bgcolor("lightgrey")
scrn1.title("Hey... It's me again!")

alita = turtle.Turtle()
alita.color("red")
alita.pencolor("red")

for i in range(3):
    alita.forward(50)
    alita.right(240)

bepo = turtle.Turtle()
bepo.color("cyan")
bepo.pencolor("cyan")

bepo.penup()
bepo.backward(25)
bepo.pendown()

for x in range(4):
    bepo.forward(100)
    bepo.right(90)
     
scrn1.mainloop()
