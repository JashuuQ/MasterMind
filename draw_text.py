import turtle

def draw_text(message, position):
    pen = turtle.Turtle()
    pen.hideturtle()
    pen.penup() 
    pen.goto(position)
    pen.write(message, align="left", font=("Arial", 14, "normal"))