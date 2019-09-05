import turtle

#Function to draw a square
def drawSquare(side, color):
    window = turtle.Screen()
    t = turtle.Turtle()
    
    t.fillcolor(color)
    t.begin_fill()

    for i in range(4):
        t.forward(side)
        t.right(90)
        
    t.end_fill()
    window.mainloop()

#Function to draw an equilateral triangle
def drawEqTriangle(side, color):
    window = turtle.Screen()
    t = turtle.Turtle()
    
    t.fillcolor(color)
    t.begin_fill()

    for i in range(3):
        t.forward(side)
        t.left(120)
        
    t.end_fill()
    window.mainloop()

#Function to draw a rectangle
def drawRectangle(width, height, color):
    window = turtle.Screen()
    t = turtle.Turtle()

    t.fillcolor(color)
    t.begin_fill()

    for i in range(4):
        if i%2 == 0:            
            t.forward(width)
        else:
            t.forward(height)
        t.right(90)
        
    t.end_fill()
    window.mainloop()

print("Let's draw shapes!")
print("**Square, Triangle, or Rectangle**")
print()
userShape = input("What shape would you like to draw? ")

if userShape.lower() == "square":
    side = input("What length should the sides be?(Pixels) ")
    side = int(side)
    color = input("What color should the square be? ")
    color = color.lower()
    
    drawSquare(side, color)
elif userShape.lower() == "triangle":
    side = input("What length should the sides be?(Pixels) ")
    side = int(side)
    color = input("What color should the triangle be? ")
    color = color.lower()
    
    drawEqTriangle(side, color)
elif userShape.lower() == "rectangle":
    width = input("How wide should the rectangle be?(Pixels) ")
    width = int(width)
    height = input("How tall should the rectangle be? ")
    height = int(height)
    color = input("What color should the rectangle be? ")
    color = color.lower()
    
    drawRectangle(width, height, color)
else:
    print("Sorry, not a valid shape")
