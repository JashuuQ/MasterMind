"""
    Name:           Jiashu Qian
    Course:         CS 5001, Fall 2023
    Subject:        Game View, Final Project
    File name:      game_view.py
    Description:    Defines the GameView class for
                        the graphical elements of the Mastermind game.
"""

import turtle

from config.window_constants import WindowConstants
from config.rec_constants import RectangleConstants
from config.text_constants import TextConstants
from config.pop_objects_constants import PopConstants
from config.board_constants import BoardConstants
from entities.rectangle import import_rectangles


class GameView:
    """
    A class to represent and manage the visual aspects of the Mastermind game.
    - Handles the drawing and updating of game elements like marbles, buttons, and popups.
    - Manages the display of the game board, including leaderboards and cursor.
    - Provides methods to show various popups for game status and errors.
    """
    def __init__(self) -> None:
        """
        Constructor - initializes the GameView object.
                    - Sets up the screen and popup_turtle properties.
        Parameters: None
        Returns: None
        """
        self.screen = None
        self.popup_turtle = None

    def set_screen(self, screen) -> None:
        """
        Method - sets up the Turtle screen.
        Parameters - screen (turtle.Screen): 
            The Turtle graphics screen object to be set up.
        Returns: None
        """
        self.screen = screen
        self.screen.setup(WindowConstants.WINDOW_WIDTH,
                          WindowConstants.WINDOW_HEIGHT)
        self.screen.title(WindowConstants.TITLE_1)

    def draw_rectangles(self):
        """
        Method - draws rectangles on the screen.
        Parameters: None
        Returns: None
        """
        import_rectangles(RectangleConstants.REC_X_1, 
                          RectangleConstants.REC_Y_1, 
                          RectangleConstants.REC_WIDTH_1, 
                          RectangleConstants.REC_HEIGHT_1, 
                          RectangleConstants.REC_COLOR_1)
        import_rectangles(RectangleConstants.REC_X_2, 
                          RectangleConstants.REC_Y_2,
                          RectangleConstants.REC_WIDTH_2, 
                          RectangleConstants.REC_HEIGHT_2, 
                          RectangleConstants.REC_COLOR_2)
        import_rectangles(RectangleConstants.REC_X_3, 
                          RectangleConstants.REC_Y_3,
                          RectangleConstants.REC_WIDTH_3, 
                          RectangleConstants.REC_HEIGHT_3, 
                          RectangleConstants.REC_COLOR_3)
    
    def load_leaderboard(self, leaderboard_data):
        """
        Method - displays the leaderboard data on the screen.
        Parameters - leaderboard_data (dict): 
            A dictionary of leaderboard names and scores.
        Returns: None
        """
        pen = turtle.Turtle()
        pen.hideturtle()
        pen.penup()
        pen.color(BoardConstants.PEN_COLOR)

        x_1 = BoardConstants.START_X_1
        y_1 = BoardConstants.START_Y_1
        pen.goto(x_1, y_1)
        pen.write(BoardConstants.TEXT, 
                  align=BoardConstants.ALIGN_1, 
                  font=BoardConstants.FONT_1)
        
        x_2 = BoardConstants.START_X_2
        y_2 = BoardConstants.START_Y_2
        line_height = BoardConstants.LINE_HEIGHT
        for index, (name, score) in enumerate(leaderboard_data.items()):
            pen.goto(x_2, y_2 - index * line_height)
            line = f"{name}: {score}"
            pen.write(line, 
                      align=BoardConstants.ALIGN_2, 
                      font=BoardConstants.FONT_2)
        
    def draw_buttons(self, buttons: list):
        """
        Method - draws interactive buttons on the screen.
        Parameters:
            buttons (list): A list of button objects to be drawn.
        Returns: None
        """
        for button in buttons:
            self.screen.addshape(button.image_path)
            butt_turtle = turtle.Turtle()
            butt_turtle.penup()
            butt_turtle.goto(button.position)
            butt_turtle.shape(button.image_path)

    def draw_marbles(self, marbles: list):
        """
        Method - draws marbles on the screen.
        Parameters:
            marbles (list): A list of marble objects to be drawn.
        Returns: None
        """
        for line_marbles in marbles:
            for marble in line_marbles:
                marble_turtle = turtle.Turtle()
                marble_turtle.hideturtle()
                marble_turtle.penup()
                marble_turtle.goto(marble.position)
                marble_turtle.down()
                marble_turtle.fillcolor(marble.color)
                marble_turtle.begin_fill()
                marble_turtle.circle(marble.size)
                marble_turtle.end_fill()
        
    def draw_cursor(self, cursor):
        """
        Method - draws a cursor on the screen.
        Parameters: cursor: The cursor object to be drawn.
        Returns: The cursor object.
        """
        return cursor
    
    def draw_text(self):
        """
        Method - draws text on the screen based on predefined constants.
        Parameters: None
        Returns: None
        """
        pen = turtle.Turtle()
        pen.hideturtle()
        pen.penup() 
        pen.goto(TextConstants.TEXT_POS)
        pen.write(TextConstants.TEXT_MESSAGE, 
                  align=TextConstants.TEXT_ALIGN, 
                  font=TextConstants.TEXT_FONT)
    
    def update_signal_marbles(self, game_engine):
        """
        Method - updates the display of signal marbles on the screen.
        Parameters:
            game_engine (GameEngine): The game's logic and state manager.
        Returns: None
        """
        self.draw_marbles(game_engine.signal_marbles)

    def update_blank_marbles(self, game_engine):
        """
        Method - updates the display of blank marbles on the screen.
        Parameters:
            game_engine (GameEngine): The game's logic and state manager.
        Returns: None
        """
        self.draw_marbles(game_engine.blank_marbles)

    def update_click_marbles(self, game_engine):
        """
        Method - updates the display of clickable marbles on the screen.
        Parameters:
            game_engine (GameEngine): The game's logic and state manager.
        Returns: None
        """
        self.draw_marbles(game_engine.click_marbles)

    def update_cursor(self, cursor):
        """
        Method - updates the cursor's position on the screen.
        Parameters:
            cursor: The cursor object to be moved.
        Returns: None
        """
        cursor.move_cursor()

    def update_view(self, game_engine):
        """
        Method - updates the entire game view on the screen.
        Parameters:
            game_engine (GameEngine): The game's logic and state manager.
        Returns: None
        """
        self.draw_buttons(game_engine.buttons)
        self.draw_cursor(game_engine.cursor)
        self.update_blank_marbles(game_engine)
        self.update_signal_marbles(game_engine)
        self.update_click_marbles(game_engine)
        turtle.update()

    def show_general_popup(self, gif_path):
        """
        Method - displays a general popup on the screen.
        Parameters:
            gif_path (str): Path to the gif image for the popup.
        Returns: None
        """
        self.popup_turtle = turtle.Turtle()
        self.popup_turtle.hideturtle()
        self.screen.addshape(gif_path) 
        self.popup_turtle.shape(gif_path)
        self.popup_turtle.showturtle()
        self.screen.update()

    def show_win_popup(self):
        """
        Method - displays the win popup.
        Parameters: None
        Returns: None
        """
        self.show_general_popup(
            PopConstants.WINNER_PATH)

    def show_lose_popup(self):
        """
        Method - displays the lose popup.
        Parameters: None
        Returns: None
        """
        self.show_general_popup(
            PopConstants.LOSE_PATH)
    
    def show_quit_popup(self):
        """
        Method - displays the quit game popup.
        Parameters: None
        Returns: None
        """
        self.show_general_popup(
            PopConstants.QUITMSG_PATH)
        
    def show_file_error(self):
        """
        Method - displays a file error popup.
        Parameters: None
        Returns: None
        """
        self.show_general_popup(
            PopConstants.FILE_ERR_PATH)
        
    def show_leaderboard_error(self):
        """
        Method - displays a leaderboard error popup.
        Parameters: None
        Returns: None
        """
        self.show_general_popup(
            PopConstants.LEADERBOARD_ERR_PATH)
        
    def close_leaderboard_error_popup(self):
        """
        Method - closes the leaderboard error popup.
        Parameters: None
        Returns: None
        """
        if self.popup_turtle:
            self.popup_turtle.hideturtle()
            self.popup_turtle.clear()
            turtle.update()
            
        