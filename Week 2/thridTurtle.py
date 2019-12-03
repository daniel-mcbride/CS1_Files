import turtle
scrn1 = turtle.Screen()
scrn1.bgcolor("lightgrey")
scrn1.title("Hello, Daniel!")
alita = turtle.Turtle()
alita.shape("turtle")		
alita.color("red")
alita.penup()                
size = 20

#run the code once outside of the loop
alita.stamp()
size = size + 3        	
alita.forward(size)       	
alita.right(24)

alita.color("white")

for i in range(29):
     alita.stamp()             	# Leave an impression on the canvas
     size = size + 3        	 	# Increase the size on every iteration
     alita.forward(size)       	# Move alita along
     alita.right(24)           	#  ...  and turn alita

alita.color("blue")
     
scrn1.mainloop()
