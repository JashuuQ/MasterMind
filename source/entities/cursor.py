"""
    Defines the Cursor class used in the Mastermind game 
        to represent the game cursor.
"""

import turtle
import math
from config.cursor_constants import CorsorConstants

class Cursor:
    """
        Manages the cursor in the Mastermind game.
        Responsible for drawing, moving, and 
            erasing the cursor on the game board.
    """
    def __init__(self, x, y) -> None:
        """
        Method - Initializes the Cursor object with its 
                    position and appearance.
        Parameters:
            x (int): The initial x-coordinate of the cursor.
            y (int): The initial y-coordinate of the cursor.
        Returns: None
        """
        self.turtle = turtle.Turtle()
        self.turtle.hideturtle()
        self.turtle.speed('fastest')
        self.x = x
        self.y = y
        self.color = CorsorConstants.CURSOR_PEN_COL
        self.fillcolor = CorsorConstants.CURSOR_FILL_COL
        self.base_length = CorsorConstants.BASE_LENGTH
        self.draw(x, y)
    
    def draw(self, x, y):
        """
        Method - Draws the cursor at a specified position.
        Parameters:
            x (int): The x-coordinate where the cursor should be drawn.
            y (int): The y-coordinate where the cursor should be drawn.
        Returns: None
        """
        self.turtle.clear()
        self.turtle.penup()
        self.turtle.goto(x, y)
        self.turtle.setheading(0) # Reset the direction
        self.turtle.fillcolor(self.fillcolor)
        self.turtle.pencolor(self.color)
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
        """
        Method - Moves the cursor to a new position 
                    based on game logic.
        Parameters: None
        Returns: None
        """
        self.erase()
        self.y -= CorsorConstants.MOVE_DIS
        self.draw(self.x, self.y)
    
    def erase(self):
        """
        Method - Erases the cursor from the screen.
        Parameters: None
        Returns: None
        """
        self.visible = False
        self.turtle.clear()