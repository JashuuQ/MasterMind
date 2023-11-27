"""
    Name:           Jiashu Qian
    Course:         CS 5001, Fall 2023
    File name:      Marble.py
    Description:    This file contains a class Marble with the attributes pen, 
                        color, position, visible, is_empty, and size. 
                    This class can draw an empty Marble and set its color, get its color, 
                        erase itself, and determine if it has been clicked.
"""
import turtle

MARBLE_RADIUS = 15

class Point:
    """
    The Point class defines a 2-dimensional point with x and y as its coordinates.
    Function delta_x(), delta_y represents the coordinate's distance 
        between this point and other points.
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def delta_x(self, other):
        return abs(self.x - other.x)

    def delta_y(self, other):
        return abs(self.y - other.y)


class Marble:
    def __init__(self, position, color, size=MARBLE_RADIUS):
        self.pen = self.new_pen()
        self.pen.hideturtle()
        self.color = color
        self.position = position
        self.visible = False
        self.is_empty = True
        self.size = size
        self.pen.speed(0)  # set to fastest drawing

    def new_pen(self): 
        return turtle.Turtle()

    def set_color(self, color):
        self.color = color
        self.is_empty = False

    def get_color(self):
        return self.color

    def draw(self):
        # if self.visible and not self.is_empty:
            # return
        self.pen.up()
        self.pen.goto(self.position.x, self.position.y)
        self.visible = True
        self.is_empty = False
        self.pen.down()
        self.pen.fillcolor(self.color)
        self.pen.begin_fill()
        self.pen.circle(self.size)
        self.pen.end_fill()

    def draw_empty(self):
        self.erase()
        self.pen.up()
        self.pen.goto(self.position.x, self.position.y)
        self.visible = True
        self.is_empty = True
        self.pen.down()
        self.pen.circle(self.size)
        
    def erase(self):
        self.visible = False
        self.pen.clear()

    def clicked_in_region(self, x, y):
        if abs(x - self.position.x) <= self.size * 2 and \
           abs(y - self.position.y) <= self.size * 2:
            return True
        return False


def main():
    marble = Marble(Point(100,100), "blue")
    marble.draw_empty()
    k = input("enter something here and I'll fill the marble > ")
    marble.draw()
    k = input("enter something here and I'll erase the marble > ")
    marble.erase()

if __name__ == "__main__":
    main()
