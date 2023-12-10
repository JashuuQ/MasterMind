"""
    Name:           Jiashu Qian
    Course:         CS 5001, Fall 2023
    Subject:        Programming Component (Tests File), Final Project
    File name:      test_mastermind_game.py
    Description:    This is a test file for our game functions, 
                        which does not test turtle/view.
"""
import unittest
from source.mastermind_game import GameEngine

TEST_CASES = [
            ['blue', 'red', 'green', 'yellow'],       # 4 Black
            ['blue', 'red', 'green', 'purple'],       # 3 Black, 1 White
            ['blue', 'red', 'yellow', 'green'],       # 2 Black, 2 Red
            ['blue', 'red', 'yellow', 'purple'],      # 2 Black, 1 Red, 1 White
            ['blue', 'red', 'purple', 'black'],       # 2 Black, 2 White
            ['blue', 'green', 'yellow', 'red'],       # 1 Black, 3 Red
            ['blue', 'green', 'yellow', 'black'],     # 1 Black, 2 Red, 1 White
            ['blue', 'green', 'purple', 'black'],     # 1 Black, 1 Red, 2 White
            ['red', 'blue', 'yellow', 'green'],       # 4 Red
            ['red', 'blue', 'yellow', 'purple'],      # 3 Red, 1 White
            ['red', 'blue', 'purple', 'black']        # 2 Red, 2 White
        ]

class TestGuessEvaluation(unittest.TestCase):
    """
    A unit test class for evaluating the guess results in the Mastermind game.
    Attributes:
        game_engine (GameEngine): An instance of the game engine for testing.
    """
    def setUp(self):
        """
        Set up the test environment by creating a game engine instance 
            and initializing the secret code.
        """
        self.game_engine = GameEngine()
        self.game_engine.secret_code = ['blue', 'red', 'green', 'yellow']

    def test_guess_evaluation(self):
        """
        Test the evaluation of guess codes.
        The evaluation includes the use of three colors:
            - Black: Indicates that the color is correct and in the correct position.
            - Red: Indicates that the color is correct but in the wrong position.
            - White: Indicates that the color is neither correct nor in the correct position.
        """
        expected_results = [
            ['black', 'black', 'black', 'black'],         # 4 Black
            ['black', 'black', 'black', 'white'],         # 3 Black, 1 White
            ['black', 'black', 'red', 'red'],             # 2 Black, 2 Red
            ['black', 'black', 'red', 'white'],           # 2 Black, 1 Red, 1 White
            ['black', 'black', 'white', 'white'],         # 2 Black, 2 White
            ['black', 'red', 'red', 'red'],               # 1 Black, 3 Red
            ['black', 'red', 'red', 'white'],             # 1 Black, 2 Red, 1 White
            ['black', 'red', 'white', 'white'],           # 1 Black, 1 Red, 2 White
            ['red', 'red', 'red', 'red'],                 # 4 Red
            ['red', 'red', 'red', 'white'],               # 3 Red, 1 White
            ['red', 'red', 'white', 'white']              # 2 Red, 2 White
        ]

        for i, guess_code in enumerate(TEST_CASES):
            self.game_engine.check_code = guess_code
            result = self.game_engine.change_signal_marbles()
            
            expected = expected_results[i]
            actual = []
            count = 0
            for color in result:
                actual.append(color)
                count += 1
            while count < 4:
                actual.append('white')
                count += 1

            self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()
