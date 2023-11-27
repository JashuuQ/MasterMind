import turtle
from rectangle import draw_rectangle
from draw_text import draw_text
from button import Button
from cursor import Cursor
from constants import *
from marble import *


def import_rectangle():
    draw_rectangle(REC_X_1, REC_Y_1, 
                   REC_WIDTH_1, REC_HEIGHT_1, REC_COLOR_1)
    draw_rectangle(REC_X_2, REC_Y_2,
                   REC_WIDTH_2, REC_HEIGHT_2, REC_COLOR_2)
    draw_rectangle(REC_X_3, REC_Y_3,
                   REC_WIDTH_3, REC_HEIGHT_3, REC_COLOR_3)

def import_button(screen):
    check_button = Button(screen, CHECK_BUTTON_PATH, CHECK_BUTT_POS)
    x_button = Button(screen, XBUTTON_PATH, XBUTTON_BUTT_POS)
    quit_button = Button(screen, QUIT_BUTTON_PATH, QUIT_BUTT_POS)


def draw_each_line(rows, columns, marble_radius, x_offset, y_offset) -> list:
    turtle.hideturtle()
    turtle.speed('fastest')
    marbles = []
    for i in range(rows):
        for j in range(columns):
            x = x_offset + j * 3 * marble_radius
            y = y_offset - i * 3 * marble_radius
            marble = Marble(Point(x, y), 'white', marble_radius)
            marble.draw()
            marbles.append(marble)
    return marbles

def draw_guess_board() -> tuple:
    cursor = Cursor(CURSOR_X, CURSOR_Y)
    x_offset = -250
    y_offset = 270
    guess_list = []
    result_list = []
    for _ in range(10):
        guess_list.append(
            draw_each_line(1, 4, MARBLE_RADIUS, 
                           x_offset, y_offset))
        result_list.append(
            draw_each_line(2, 2, MARBLE_RADIUS//3, 
                           x_offset + 260, y_offset + 20))
        y_offset -= 50
    return guess_list, result_list

def draw_button_board() -> list:
    draw_text('Click the matching color peg to place it in the row.', 
              (-300, -270))
    x = -270
    y = -310

    button_list = []
    for color in COLORS:
        marble = Marble(Point(x, y), color, MARBLE_RADIUS)
        marble.draw()
        button_list.append(marble)
        x += 45
    
    return button_list
