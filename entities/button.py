"""
    Defines the Button class used in the Mastermind game 
        to represent interactive buttons.
"""
import math
from config.button_constants import ButtonConstants

class Button:
    """
    The Button class manages the properties and behaviors of game buttons, 
        including their size, position, and interaction logic.
    """
    def __init__(self, image_path, position, button_type):
        """
        Method - Initializes the Button object with its image, position, and type.
        Parameters:
            image_path (str): Path to the button's image.
            position (tuple): The (x, y) coordinates 
                of the button's position.
            button_type (str): Type of the button 
                ('check_button', 'x_button', 'quit_button').
        Returns: None
        """
        self.position = position
        self.image_path = image_path
        self.button_type = button_type
        self.width, self.height = self.get_button_size(button_type)

    def get_button_size(self, button_type):
        """
        Method - Determines the size of the button based on its type.
        Parameters:
            button_type (str): The type of the button.
        Returns: Tuple of (width, height) of the button.
        """
        size_lst = ButtonConstants.BUTT_SIZE
        if button_type == 'check_button':
            return size_lst[0][0], size_lst[0][1]
        elif button_type == 'x_button':
            return size_lst[1][0], size_lst[1][1]
        elif button_type == 'quit_button':
            return size_lst[2][0], size_lst[2][1]

    def click_in_region(self, x, y):
        """
        Method - Checks if a given point (x, y) is 
                    within the button's click region.
        Parameters:
            x (float): The x-coordinate of the point.
            y (float): The y-coordinate of the point.
        Returns: Boolean indicating if the point is 
                    within the button's click region.
        """
        if self.button_type in ['check_button', 'x_button']: 
            radius = self.width / 2
            center_x, center_y = self.position
            distance = math.sqrt((x - center_x) ** 2 + (y - center_y) ** 2)
            return distance <= radius
        elif self.button_type == 'quit_button':
            x_1, y_1 = self.position    # Top-left corner coordinates
            x_2, y_2 = x_1 + self.width, y_1 - self.height
            return x_1 <= x <= x_2 and y_2 <= y <= y_1