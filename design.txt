MasterMind Design Document:

1. Testing:
This document outlines our testing and the main Mastermind game code.

2. Test Cases:
We used these test cases:
['blue', 'red', 'green', 'yellow']: 4 Black
['blue', 'red', 'green', 'purple']: 3 Black, 1 White
['blue', 'red', 'yellow', 'green']: 2 Black, 2 Red
['blue', 'red', 'yellow', 'purple']: 2 Black, 1 Red, 1 White
['blue', 'red', 'purple', 'black']: 2 Black, 2 White
['blue', 'green', 'yellow', 'red']: 1 Black, 3 Red
['blue', 'green', 'yellow', 'black']: 1 Black, 2 Red, 1 White
['blue', 'green', 'purple', 'black']: 1 Black, 1 Red, 2 White
['red', 'blue', 'yellow', 'green']: 4 Red
['red', 'blue', 'yellow', 'purple']: 3 Red, 1 White
['red', 'blue', 'purple', 'black']: 2 Red, 2 White

3. Test GuessEvaluation Class:
    A unit test class for evaluating guess results, with an attribute:
    - game_engine (GameEngine): Used for testing.

4. Test Setup:
    We create a game engine instance and initialize the secret code.

5. Test GuessEvaluation Method:
    Tests guess evaluation, including Black, Red, and White indicators.

6. Expected Results:
    Provided for each test case for assertions.

7. Main Program:
    Includes core Mastermind game functionalities: 
        initialization, board setup, status handling, and mouse click handling.

8. Main Program Flow:
- Initialize Turtle graphics settings.
- Prompt player for name.
- Set up game board.
- Handle game status and mouse clicks.
- Start game loop.