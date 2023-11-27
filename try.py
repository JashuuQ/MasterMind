import turtle
from marble import *


def draw_each_line(rows, cols, marble_radius, x_offset, y_offset):
    turtle.speed(0)
    turtle.hideturtle()
    marbles = []
    for i in range(rows):
        row = []
        for j in range(cols):
            x = x_offset + j * 3 * marble_radius
            y = y_offset - i * 3 * marble_radius
            marble = Marble(Point(x, y), 'white', marble_radius)
            marble.draw()
            row.append(marble)
        marbles.append(row)
    return marbles

def draw_guess_board():
    x_offset = -150
    y_offset = 250
    for _ in range(10):
        test_board = draw_guess_board(1, 4, MARBLE_RADIUS, x_offset, y_offset)
        result_board = draw_guess_board(2, 2, MARBLE_RADIUS//3, x_offset + 300, y_offset + 20)
        y_offset -= 50

def main():
    screen = turtle.Screen()
    screen.setup(width=800, height=1050)
    screen.tracer(0)  # Disable automatic screen updates for faster drawing
    draw_guess_board()

    screen.update()  # Update the screen after all drawing commands
    

if __name__ == "__main__":
    main()
    turtle.mainloop()
