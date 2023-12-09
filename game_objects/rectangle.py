"""
    Contains the function import_rectangles to 
        draw rectangles in the Mastermind game using Turtle graphics.
"""
import turtle

from game_config.rec_constants import RectangleConstants

def import_rectangles(x, y, width, height, color='black'):
    """
    Method - Draws a rectangle using Turtle 
                graphics at specified coordinates.
    Parameters:
        x (int): The x-coordinate of the rectangle's starting point.
        y (int): The y-coordinate of the rectangle's starting point.
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
        color (str): The color of the rectangle's outline.
    Returns: None
    """
    rec = turtle.Turtle()
    rec.hideturtle()
    rec.pensize(RectangleConstants.REC_PENSIZE)
    rec.pencolor(color)
    rec.speed(0)
    rec.penup()
    rec.goto(x, y)
    rec.pendown()
    for _ in range(2):
        rec.forward(width)
        rec.right(90)
        rec.forward(height)
        rec.right(90)
    rec.penup()
    