"""
    Name:           Jiashu Qian
    Course:         CS 5001, Fall 2023
    Subject:        Game Engine, Final Project
    File name:      game_engine.py
    Description:    Defines the GameEngine class for
                        the graphical elements of the Mastermind game.
"""
import random

from config.button_constants import ButtonConstants
from config.marble_constants import MarbleConstants
from config.cursor_constants import CorsorConstants
from config.config_files import CONFIG_FILES

from entities.button import Button
from entities.marble import Marble
from entities.cursor import Cursor


class GameEngine:
    """
    A class to manage the core mechanics and state of the Mastermind game.
    - Provides methods for creating game components 
        like buttons, cursor, and marbles.
    - Handles game logic including checking clicks, 
        updating game state, and managing secret code.
    - Maintains counters for player's actions and the game's progress.
    """
    def __init__(self) -> None:
        """
        Constructor - initializes the GameEngine object.
        Parameters: None
        Returns: None
        """
        # Create buttons and cursor
        self.buttons = self.__build_buttons__()
        self.check_button = self.buttons[0]
        self.x_button = self.buttons[1]
        self.quit_button = self.buttons[2]
        self.cursor = self.__build_cursor__()
        # Create marbles
        self.blank_marbles = self.__build_blank_marbles__()
        self.signal_marbles = self.__build_signal_marbles__()
        self.click_marbles = self.__build_click_marbles__()
        # Count clicks, lines
        self.click_count = 0
        self.line_count = 0
        # Store secret_code and check_code
        self.secret_code = self.generate_secret_code()
        self.check_code = []
        self.black_num = 0
        # Mark the status of the game
        self.status = ''
        self.game_over = False

    def __build_buttons__(self) -> list:
        """
        Method - creates button objects for the game.
        Parameters: None
        Returns: list of Button objects
        """
        check_button = Button(ButtonConstants.CHECK_BUTTON_PATH, 
                              ButtonConstants.CHECK_BUTT_POS, 
                              ButtonConstants.CHECK_TYPE)
        x_button = Button(ButtonConstants.XBUTTON_PATH, 
                          ButtonConstants.XBUTTON_BUTT_POS, 
                          ButtonConstants.X_TYPE)
        quit_button = Button(ButtonConstants.QUIT_BUTTON_PATH, 
                             ButtonConstants.QUIT_BUTT_POS, 
                             ButtonConstants.QUIT_TYPE)
        return [check_button, x_button, quit_button]

    def __build_cursor__(self):
        """
        Method - creates a cursor object for the game.
        Parameters: None
        Returns: Cursor object
        """
        cursor = Cursor(CorsorConstants.CURSOR_X,
                        CorsorConstants.CURSOR_Y)
        return cursor

    def __build_blank_marbles__(self) -> list:
        """
        Method - creates blank marble objects for the game.
        Parameters: None
        Returns: Nested list of Marble objects
        """
        blank_marbles = []
        x_offset = MarbleConstants.BLANK_MARBLE_X
        y_offset = MarbleConstants.BLANK_MARBLE_Y
        for _ in range(10):
            line_marbles = []
            for i in range(1):
                for j in range(4):
                    x = x_offset + j * 3 * MarbleConstants.MARBLE_RADIUS
                    y = y_offset - i * 3 * MarbleConstants.MARBLE_RADIUS
                    marble = Marble((x, y), 'white', MarbleConstants.MARBLE_RADIUS)
                    line_marbles.append(marble)
            blank_marbles.append(line_marbles)
            y_offset -= MarbleConstants.MARBLE_GAP_1
        return blank_marbles # Nested list

    def __build_signal_marbles__(self) -> list:
        """
        Method - creates signal marble objects for the game.
        Parameters: None
        Returns: Nested list of Marble objects
        """
        signal_marbles = []
        x_offset = MarbleConstants.SIGNAL_MARBLE_X
        y_offset = MarbleConstants.SIGNAL_MARBLE_Y
        signal_radius = MarbleConstants.MARBLE_RADIUS // 3
        for _ in range(10):
            line_marbles = []
            for i in range(2):
                for j in range(2):
                    x = x_offset + j * 3 * signal_radius
                    y = y_offset - i * 3 * signal_radius
                    signal = Marble((x, y), 'white', signal_radius)
                    line_marbles.append(signal)
            signal_marbles.append(line_marbles)
            y_offset -= MarbleConstants.MARBLE_GAP_2
        return signal_marbles # Nested list
    
    def __build_click_marbles__(self) -> list:
        """
        Method - creates clickable marble objects for the game.
        Parameters: None
        Returns: List of Marble objects
        """
        click_marbles = []
        x = MarbleConstants.CLICK_MARBLE_X
        y = MarbleConstants.CLICK_MARBLE_Y
        for color in MarbleConstants.COLORS:
            marble = Marble((x, y), color, MarbleConstants.MARBLE_RADIUS)
            click_marbles.append(marble)
            x += MarbleConstants.MARBLE_GAP_3
        return [click_marbles]

    def check_config_exists(self, config_folder):
        """
        Method - checks if configuration files exist in the specified folder.
        Parameters:
            config_folder (str): The folder to check for configuration files.
        Returns: bool indicating the existence of config files
        """
        missing_files = []
        for file_name in CONFIG_FILES:
            try:
                with open(f"{config_folder}/{file_name}") as f:
                    pass
            except FileNotFoundError:
                missing_files.append(file_name)
        if missing_files:
            missing_files_str = ', '.join(missing_files)
            print(f"Missing configuration files: {missing_files_str}")
            return False
        return True
    
    def generate_secret_code(self) -> list:
        """
        Method - generates a secret code for the game.
        Parameters: None
        Returns: List of colors representing the secret code
        """
        return random.sample(MarbleConstants.COLORS, 4)

    # Click - click_marbles
    def check_if_marble_clicked(self, x, y):
        """
        Method - checks if a marble has been clicked.
        Parameters:
            x (float): The x-coordinate of the click.
            y (float): The y-coordinate of the click.
        Returns: Marble object or False
        """
        for click_marble in self.click_marbles[0]:
            if click_marble.clicked_in_region(x, y) and \
                click_marble.color != 'white':
                return click_marble
        return False

    def choose_marble_color(self, x, y):
        """
        Method - sets the color of a marble based on a click.
        Parameters:
            x (float): The x-coordinate of the click.
            y (float): The y-coordinate of the click.
        Returns: None
        """
        line = self.line_count
        clicked_marble = self.check_if_marble_clicked(x, y)
        if clicked_marble and self.click_count < 4:
            self.blank_marbles[line][self.click_count].color = \
                    clicked_marble.get_color()
            self.check_code.append(clicked_marble.get_color())
            clicked_marble.color = 'white'
            self.click_count += 1
    
    # Click - check_buttons
    def check_if_check_butt_clicked(self, x, y):
        """
        Method - checks if the check button has been clicked.
        Parameters:
            x (float): The x-coordinate of the click.
            y (float): The y-coordinate of the click.
        Returns: True if the check button is clicked, otherwise False
        """
        if self.click_count != 0 and \
            self.click_count % 4 == 0:
            if self.check_button.click_in_region(x, y):
                return True
        return False
    
    def change_signal_marbles(self):
        """
        Method - updates the signal marbles based on the player's guess.
        Parameters: None
        Returns: List of results ('black' or 'red') for each marble
        """
        guess_result = []
        for i, item in enumerate(self.check_code):
            for j, color in enumerate(self.secret_code):
                if item == color:
                    if i == j:
                        guess_result.append('black')
                        self.black_num += 1
                    else:
                        guess_result.append('red')
        guess_result = sorted(guess_result)

        # Change the color of signal marbles in this line
        line_signal_marbles = self.signal_marbles[self.line_count]
        for i, color in enumerate(guess_result):
                line_signal_marbles[i].color = color

        return guess_result
    
    def check_guess_status(self):
        """
        Method - checks the current status of the player's guess.
        Parameters: None
        Returns: None
        """
        if self.black_num == 4:
            self.status = 'win'
            self.game_over = True
        elif self.line_count == 9:
            self.status = 'lose'
            self.game_over = True
        else:
            self.status = 'continue'

    def click_check_button(self, x, y) -> tuple:
        """
        Method - processes a click on the check button.
        Parameters:
            x (float): The x-coordinate of the click.
            y (float): The y-coordinate of the click.
        Returns: Current game status as a string, or None
        """
        if self.check_if_check_butt_clicked(x, y):
            self.change_signal_marbles()
            self.click_marbles = self.__build_click_marbles__()
            self.check_guess_status()
            if self.status == 'continue':
                self.cursor.move_cursor()
                self.line_count += 1
                self.click_count = 0
                self.check_code = []
                self.black_num = 0
            return self.status
        return None
    
    # Click - x_buttons
    def check_if_x_butt_clicked(self, x, y):
        """
        Method - checks if the X button has been clicked.
        Parameters:
            x (float): The x-coordinate of the click.
            y (float): The y-coordinate of the click.
        Returns: True if the X button is clicked, otherwise False
        """
        if self.x_button.click_in_region(x, y):
            return True
        return False
    
    def change_blank_marbles(self):
        """
        Method - resets the colors of the blank marbles 
                    in the current line.
        Parameters: None
        Returns: None
        """
        line = self.line_count
        for i in range(4):
            self.blank_marbles[line][i].color = 'white'
    
    def click_x_button(self, x, y):
        """
        Method - processes a click on the X button.
        Parameters:
            x (float): The x-coordinate of the click.
            y (float): The y-coordinate of the click.
        Returns: None
        """
        if self.check_if_x_butt_clicked(x, y):
            self.change_blank_marbles()
            self.click_marbles = self.__build_click_marbles__()
            self.click_count = 0
            self.check_code = []
            self.black_num = 0
        return None

    # Click - quit_buttons
    def check_if_quit_butt_clicked(self, x, y):
        """
        Method - checks if the quit button has been clicked.
        Parameters:
            x (float): The x-coordinate of the click.
            y (float): The y-coordinate of the click.
        Returns: True if the quit button is clicked, otherwise False
        """
        if self.quit_button.click_in_region(x, y):
            return True
        return False
    
    def click_quit_button(self, x, y):
        """
        Method - processes a click on the quit button.
        Parameters:
            x (float): The x-coordinate of the click.
            y (float): The y-coordinate of the click.
        Returns: True if the game is to be quit, otherwise None
        """
        if self.check_if_quit_butt_clicked(x, y):
            return True
        return None
    
