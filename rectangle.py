import turtle

REC_PENSIZE = 5

def draw_rectangle(x, y, width, height, color='black'):
    rec = turtle.Turtle()
    rec.pensize(REC_PENSIZE)
    rec.pencolor(color)
    rec.speed(0)
    rec.hideturtle()
    rec.penup()
    rec.goto(x, y)
    rec.pendown()
    for _ in range(2):
        rec.forward(width)
        rec.right(90)
        rec.forward(height)
        rec.right(90)
    rec.penup()
    