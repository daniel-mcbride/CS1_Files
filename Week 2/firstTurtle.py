import turtle
window= turtle.Screen()#Create the screen for drawing
window.bgcolor("cyan") #Set a background color for the created screen
bepo=turtle.Turtle()   #Create a turtle set to the bepo variable
bepo.forward(50)       #Move bepo forward 50 pixels
bepo.left(90)          #Rotate bepo left 90 degrees
bepo.forward(100)      #Move bepo forward 100 pixels

#Create top of rectangle
bepo.left(90)
bepo.forward(50)

#Create left sede of rectangle
bepo.left(90)
bepo.forward(100)

window.mainloop()      #REQUIRED!! Tells the program to close when the screen is closed
