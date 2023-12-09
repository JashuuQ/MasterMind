"""
    Defines the RectangleConstants class in the Mastermind game,
    storing constant values for the dimensions and positions 
        of rectangles used in the game's interface.
"""

from game_config.window_constants import WindowConstants

class RectangleConstants:
    """
        Stores constant values related to the dimensions, 
            positions, and colors of rectangles
    """
    REC_PENSIZE = 5
    
    SMALL_GAP = 15
    BIG_GAP = 25

    REC_WIDTH_1 = 450
    REC_HEIGHT_1 = 550
    REC_X_1 = SMALL_GAP - WindowConstants.WINDOW_WIDTH / 2
    REC_Y_1 = WindowConstants.WINDOW_HEIGHT / 2 - SMALL_GAP
    REC_COLOR_1 = 'black'

    REC_WIDTH_2 = WindowConstants.WINDOW_WIDTH - 2 * SMALL_GAP \
                    - REC_WIDTH_1 - BIG_GAP - 5     # default pensize is 5
    REC_HEIGHT_2 = REC_HEIGHT_1
    REC_X_2 = REC_X_1 + REC_WIDTH_1 + BIG_GAP
    REC_Y_2 = REC_Y_1
    REC_COLOR_2 = 'blue'

    REC_WIDTH_3 = REC_WIDTH_1 + REC_WIDTH_2 + BIG_GAP
    REC_HEIGHT_3 = WindowConstants.WINDOW_HEIGHT \
                    - REC_HEIGHT_1 - 3 * SMALL_GAP
    REC_X_3 = REC_X_1
    REC_Y_3 = - WindowConstants.WINDOW_HEIGHT / 2 + SMALL_GAP + REC_HEIGHT_3
    REC_COLOR_3 = 'black'
