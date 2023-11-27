"""
    Name:           Jiashu Qian
    Course:         CS 5001, Fall 2023
    Subject:        Programming Component (Main Function), Final Project
    File name:      mastermind_game.py
    Description:    This is the main function of our mastermind game.
"""
import turtle as t
from constants import *
from set_basic_board import *

def get_player_name(screen) -> str:
    player_name = screen.textinput(TITLE, 'Your name: ')
    return player_name

def set_basic_board(screen):
    import_rectangle()
    import_button(screen)
    draw_guess_board()
    draw_button_board()


def main():
    screen = t.Screen()
    screen.setup(WINDOW_WIDTH, WINDOW_HEIGHT)
    screen.title(TITLE)

    get_player_name(screen)
    set_basic_board(screen)
    

    t.mainloop()


if __name__ == '__main__':
    main()