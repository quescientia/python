import turtle

t = turtle.Turtle()
#============

#t.color("red")
#t.circle(100)
colors = ["red", "blue", "green", "yellow"]

for i in range(4):
    t.color(colors[i])
    t.forward(200)
    t.left(90)




#============
t.screen.mainloop()