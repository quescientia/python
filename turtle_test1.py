import turtle

t = turtle.Turtle()
#t.hideturtle()
t.speed(0)
colors = ['red', 'blue','green','orange','purple','black', 'brown', 'violet']


# drawing a line
def example0():
    t.forward(150)

# drawing a square
def example1():
    for i in range(4):
        t.forward(150)
        t.left(90)

# letting the imagination run
# drawing lines to form a concentric square pattern
def example2():
    for i in range(180):
        t.forward(i)
        t.left(90)

# letting the imagination run
# changing the angle by just 1 degree 
def example3():
    for i in range(180):
        t.forward(i)
        t.left(89)

# letting the imagination run
# adding colors 
# change 89 to 88 or 87
def example4():
    for i in range(180):
        t.forward(i)
        t.color(colors[i%4])
        t.left(89)

# playing with each parameter
# change the range
# change the length
# change the direction of curve
# changing the number of sides
# match the color with no. of sides
def example5():
    for i in range(180):
        t.forward(i)
        t.color(colors[i%4])
        t.left(90)

# two loops?
def example6():
    for i in range(180):
        t.color(colors[i%2])
        t.forward(i)
        t.left(181)
    t.goto(0, 0)
    for i in range(180):
        t.color(colors[i%2])
        t.forward(i)
        t.right(181)

# two loops with specific colors
def example7():
    t.left(90)
    col = 'white'
    for i in range(180):
        if col == 'green':
            col = 'white'
        else:
            col = 'green'
        t.color(col)
        t.forward(i)
        t.left(-181)
    t.goto(0, 0)
    col = 'green'
    for i in range(180):
        if col == 'green':
            col = 'white'
        else:
            col = 'green'
        t.color(col)
        t.forward(i)
        t.left(-179)


example7()

t.screen.mainloop()