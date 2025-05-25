import turtle


pen = turtle.Turtle()
pen.hideturtle()
pen.speed(2)

def draw_circle(x,y,radius=25):
    pen.penup()
    pen.color("red")
    pen.width(5)
    pen.setpos(x,y)
    pen.pendown()
    pen.circle(radius)


pen.screen.onclick(draw_circle)



## last line
pen.screen.mainloop()
