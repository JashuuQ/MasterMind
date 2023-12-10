"""
    Name:           Jiashu Qian
    Course:         CS 5001, Fall 2023
    Subject:        Main Function, Final Project
    File name:      mastermind_game.py
    Description:    This is the main function of our mastermind game.
"""

import turtle as turtle
import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from game_view import GameView
from game_engine import GameEngine
from game_board import LeaderBoard
from config.window_constants import WindowConstants

def turtle_setup():
    """
    Function - initializes the Turtle graphics settings for the game.
    Parameters: None
    Returns: None
    """
    turtle.speed(0)
    turtle.delay(0)
    turtle.tracer(False)
    turtle.hideturtle()

def get_player_name(screen) -> str:
    """
    Function - prompts the player to input their name.
             - Uses the Turtle screen's text input method.
    Parameters:
        screen (turtle.Screen): The Turtle graphics screen object.
    Returns:
        str: The player's name as entered.
    """
    player_name = screen.textinput(
                    WindowConstants.TITLE_1, 'Your name: ')
    return player_name

def set_basic_board(game_engine, game_view, 
                    leader_board, screen):
    """
    Function - sets up the basic components of the game board.
    Parameters:
        game_engine (GameEngine): The game's logic and state manager.
        game_view (GameView): The game's view renderer.
        leader_board (LeaderBoard): The game's leaderboard manager.
        screen (turtle.Screen): The Turtle graphics screen object.
    Returns: None
    """
    leaderboard_data = leader_board.read_leader_board()
    if leaderboard_data == 'FileNotFound':
        game_view.show_leaderboard_error()
        screen.ontimer(
            game_view.close_leaderboard_error_popup, 2000)
        
    game_view.draw_rectangles()
    game_view.draw_text()
    if isinstance(leaderboard_data, dict):
        game_view.load_leaderboard(leaderboard_data)
    game_view.update_view(game_engine)
    
def lose_and_show_code(screen, game_engine):
    """
    Function - displays the secret code to the player upon losing.
    Parameters:
        screen (turtle.Screen): The Turtle graphics screen object.
        game_engine (GameEngine): The game's logic and state manager.
    Returns: None
    """
    secret_code = game_engine.secret_code
    screen.textinput(
            WindowConstants.TITLE_2, secret_code)

def handle_game_status(status, screen, game_engine, game_view):
    """
    Function - handles the game's status based on the player's actions.
    Parameters:
        status (str): The current status of the game ('win', 'lose', or None).
        screen (turtle.Screen): The Turtle graphics screen object.
        game_engine (GameEngine): The game's logic and state manager.
        game_view (GameView): The game's view renderer.
    Returns: None
    """
    game_view.update_signal_marbles(game_engine)
    game_view.update_click_marbles(game_engine)
    if game_engine.game_over:
        show_end_game_popup(status, screen, game_engine, game_view)
        if status == 'win' or status == 'lose':
            screen.ontimer(lambda: screen.bye(), 1500)

def show_end_game_popup(status, screen, game_engine, game_view):
    """
    Function - Displays either a 'win' or 'lose' popup, \
                and reveals the secret code if lost.
    Parameters:
        status (str): The current status of the game ('win' or 'lose').
        screen (turtle.Screen): The Turtle graphics screen object.
        game_engine (GameEngine): The game's logic and state manager.
        game_view (GameView): The game's view renderer.
    Returns: None
    """
    if status == 'win':
        game_view.show_win_popup()
    elif status == 'lose':
        game_view.show_lose_popup()
        lose_and_show_code(screen, game_engine)

def handle_click(x, y, screen, game_engine, game_view):
    """
    Function - handles mouse click events on the game screen.
    Parameters:
        x (float): The x-coordinate of the click.
        y (float): The y-coordinate of the click.
        screen (turtle.Screen): The Turtle graphics screen object.
        game_engine (GameEngine): The game's logic and state manager.
        game_view (GameView): The game's view renderer.
    Returns: None
    """
    # If click the click_marbles
    game_engine.choose_marble_color(x, y)
    game_view.update_blank_marbles(game_engine)
    game_view.update_click_marbles(game_engine)

    # If click the check_button
    status = game_engine.click_check_button(x, y)
    if status:
        handle_game_status(status, screen, game_engine, game_view)

    # If click the quit_button
    if game_engine.click_quit_button(x, y):
        game_view.show_quit_popup()
        screen.ontimer(lambda: screen.bye(), 1500)
        return

    # If click the x_button
    game_engine.click_x_button(x, y)
    game_view.update_blank_marbles(game_engine)
    game_view.update_click_marbles(game_engine)


def main():
    """
        Sets up the game environment, 
        initializes game components, 
            and starts the game loop. 
    """
    screen = turtle.Screen()
    turtle_setup()
    game_view = GameView()
    game_engine = GameEngine()
    leader_board = LeaderBoard()

    new_name = get_player_name(screen)
    game_view.set_screen(screen)

    if not game_engine.check_config_exists("config"):
        game_view.show_file_error()
        screen.ontimer(lambda: screen.bye(), 1500)
        return
    
    set_basic_board(game_engine, game_view, 
                    leader_board, screen)

    def on_screen_click(x, y):
        """
        Function - Manages game interactions based on \
                    user clicks and updates the game state accordingly.
        Parameters:
            x (float): The x-coordinate of the the click occurred.
            y (float): The y-coordinate of the the click occurred.
        Returns: None
        """
        handle_click(x, y, screen, game_engine, game_view)
        if game_engine.game_over:
            new_score = game_engine.line_count
            leader_board.update_leaderboard(new_score, new_name)
    screen.onscreenclick(on_screen_click)

    turtle.mainloop()


if __name__ == '__main__':
    main()