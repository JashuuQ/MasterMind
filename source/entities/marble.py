"""
    Defines the Marble class used in the Mastermind game 
        for representing individual marbles.
"""

import turtle

from config.marble_constants import MarbleConstants

class Marble:
    """
    Represents a marble in the Mastermind game.
    Manages marble's color, position, visibility, and drawing operations.
    """
    def __init__(self, position, color, 
                 size=MarbleConstants.MARBLE_RADIUS):
        """
        Method - Initializes the Marble object with position, color, and size.
        Parameters:
            position (tuple): The (x, y) coordinates of the marble's position.
            color (str): The color of the marble.
            size (int): The radius of the marble.
        Returns: None
        """
        self.pen = self.new_pen()
        self.pen.hideturtle()
        self.color = color
        self.position = position
        self.visible = False
        self.is_empty = True
        self.size = size
        self.pen.speed(0)  # set to fastest drawing

    def new_pen(self):
        """
        Method - Creates a new Turtle object for drawing.
        Parameters: None
        Returns: Turtle object
        """
        return turtle.Turtle()

    def set_color(self, color):
        """
        Method - Sets the color of the marble and updates its state.
        Parameters:
            color (str): The new color to set for the marble.
        Returns: None
        """
        self.color = color
        self.is_empty = False

    def get_color(self):
        """
        Method - Gets the current color of the marble.
        Parameters: None
        Returns: The color of the marble as a string.
        """
        return self.color

    def draw(self):
        """
        Method - Draws the marble on the screen.
        Parameters: None
        Returns: None
        """
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
        """
        Method - Draws an empty representation of the marble.
        Parameters: None
        Returns: None
        """
        self.erase()
        self.pen.up()
        self.pen.goto(self.position[0], self.position[1])
        self.visible = True
        self.is_empty = True
        self.pen.down()
        self.pen.circle(self.size)
        
    def erase(self):
        """
        Method - Erases the marble from the screen.
        Parameters: None
        Returns: None
        """
        self.visible = False
        self.pen.clear()

    def clicked_in_region(self, x, y):
        """
        Method - Checks if a given point (x, y) 
                    is within the marble's region.
        Parameters:
            x (float): The x-coordinate of the point.
            y (float): The y-coordinate of the point.
        Returns: Boolean indicating if the point 
                    is within the marble's region.
        """
        distance = ((x - self.position[0]) ** 2 + 
                    (y - self.position[1]) ** 2) ** 0.5
        if distance <= self.size:
            return True
        return False