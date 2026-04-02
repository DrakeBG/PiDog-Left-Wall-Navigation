import turtle             # Allows us to use turtles
wn = turtle.Screen()      # Creates a playground for turtles
alex = turtle.Turtle()    # Create a turtle, assign to alex

for i in range(1,1000,100):
    alex.forward(100+i)          # Tell alex to move forward by 150 units
    alex.left(50)             # Tell alex to turn by 90 degrees
    alex.forward(100+i)          # Complete the second side of a rectangle
    alex.left(50)
    alex.forward(100+i)
    alex.left(50)
    alex.forward(100+i)
    alex.penup()
    alex.right(45)
    alex.forward((2**0.5)*50)
    alex.pendown()
    alex.left(135)