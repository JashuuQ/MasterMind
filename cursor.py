import turtle
import math

CURSOR_PEN_COL = 'black'
CURSOR_FILL_COL = 'red'
BASE_LENGTH = 25
MOVE_DIS = 20

class Cursor:
    def __init__(self, x, y) -> None:
        self.turtle = turtle.Turtle()
        self.turtle.hideturtle()
        self.turtle.speed('fastest')
        self.x = x
        self.y = y
        self.color = CURSOR_PEN_COL
        self.fillcolor = CURSOR_FILL_COL
        self.base_length = BASE_LENGTH
        self.draw(x, y)
    
    def draw(self, x, y):
        self.turtle.penup()
        self.turtle.goto(x, y)
        self.turtle.fillcolor(self.fillcolor)
        self.turtle.begin_fill()
        self.turtle.pendown()

        self.turtle.left(30)
        self.turtle.forward(self.base_length)
        self.turtle.left(120)
        self.turtle.forward(self.base_length)
        self.turtle.left(150)
        self.turtle.forward(self.base_length / math.sqrt(3))
        self.turtle.right(60)
        self.turtle.forward(self.base_length / math.sqrt(3))

        self.turtle.end_fill()


    def move_cursor(self):
        self.turtle.goto(self.x, self.y - MOVE_DIS)


        