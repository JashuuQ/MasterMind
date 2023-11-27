"""
This is a file that has all the constants in the game.
"""

WINDOW_WIDTH = 700
WINDOW_HEIGHT = 700

TITLE = "CS5001_MasterMind_Jiashu Qian"

# === Constants of the basic rectangle board ===
SMALL_GAP = 15
BIG_GAP = 25

REC_WIDTH_1 = 450
REC_HEIGHT_1 = 550
REC_X_1 = SMALL_GAP - WINDOW_WIDTH / 2
REC_Y_1 = WINDOW_HEIGHT / 2 - SMALL_GAP
REC_COLOR_1 = 'black'

REC_WIDTH_2 = WINDOW_WIDTH - 2 * SMALL_GAP \
                - REC_WIDTH_1 - BIG_GAP - 5     # default pensize is 5
REC_HEIGHT_2 = REC_HEIGHT_1
REC_X_2 = REC_X_1 + REC_WIDTH_1 + BIG_GAP
REC_Y_2 = REC_Y_1
REC_COLOR_2 = 'blue'

REC_WIDTH_3 = REC_WIDTH_1 + REC_WIDTH_2 + BIG_GAP
REC_HEIGHT_3 = WINDOW_HEIGHT - REC_HEIGHT_1 - 3 * SMALL_GAP
REC_X_3 = REC_X_1
REC_Y_3 = - WINDOW_HEIGHT / 2 + SMALL_GAP + REC_HEIGHT_3
REC_COLOR_3 = 'black'


# === Constants of the Button ===
CHECK_BUTTON_PATH = 'button_board/checkbutton.gif'
XBUTTON_PATH = 'button_board/xbutton.gif'
QUIT_BUTTON_PATH = 'button_board/resized_quit.gif'

CHECK_BUTT_POS = (60, -282)
XBUTTON_BUTT_POS = (140, -282)
QUIT_BUTT_POS = (250, -282)

# === Constants of the Corsor ===
CURSOR_X = -300
CURSOR_Y = 270

# === Constants of the Marble ===
MARBLE_X = -275
MARBLE_Y = 275
MARBLE_RADIUS = 15

# === Constants of the guess_board ===
COLORS = ["blue", "red", "green", "yellow", "purple", "black"]