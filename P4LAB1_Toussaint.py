# Nexabet Toussaint
# 11/7/2024
# P4LAB1
#Draw a square and a triangle with the turtle library

# While loop to draw square

import turtle
win = turtle.Screen()
t = turtle.Turtle()
win.bgcolor("purple")

t.pensize(8)
t.shape("arrow")
t.pencolor("red")

# while loop for the square

num = 0

while num <4:
    t.forward(150)
    t.right(90)
    num += 1
print("while loop ends")


# For loop to draw a triangle
for tr in range(0,3):
    t.forward(100)
    t.left(120)

turtle.done()
    
