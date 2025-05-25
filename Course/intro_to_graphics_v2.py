

import turtle
import time

colors = ["red", "blue", "green", "purple"]

number_of_sides = int(input("Enter the number of sides: "))
a = 360/number_of_sides
pen = turtle.Turtle()
for i in range(number_of_sides*20):
    pen.color(colors[i%4])
    pen.forward(360/number_of_sides)
    pen.left(a)


## last line to keep the graphics on the screen

pen.screen.mainloop()