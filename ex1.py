# Use turtle graphics to make an infinite spiral
import turtle
turtle.speed
i = 0 # i is indexing variable
num = 30 # num is the line segment
while i < num:
    turtle.forward (20*i) #makes progressively large line segments 
    turtle.right(90)
    i = i + 1