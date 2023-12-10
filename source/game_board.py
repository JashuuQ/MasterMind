"""
    Name:           Jiashu Qian
    Course:         CS 5001, Fall 2023
    Subject:        Game Board, Final Project
    File name:      game_board.py
    Description:    Defines the LeaderBoard class for
                        the graphical elements of the Mastermind game.
"""

from config.pop_objects_constants import PopConstants

class LeaderBoard:
    """
    A class to manage the leaderboard for the Mastermind game.
    - Handles the reading and writing of leaderboard data to a file.
    - Provides methods for updating and rewriting the leaderboard with new scores.
    """
    def __init__(self, 
                file_name=PopConstants.LEADERBOARD_FILE,
                max_entries=PopConstants.MAX_ENTRIES) -> None:
        """
        Constructor - initializes the LeaderBoard object.
        Parameters:
            file_name (str): The file path for storing leaderboard data.
            max_entries (int): The maximum number of entries.
        Returns: None
        """
        self.file_name = file_name
        self.max_entries = max_entries

    def read_leader_board(self):
        """
        Method - reads the leaderboard data from a file.
        Parameters: None
        Returns: Dictionary of leaderboard data or 'FileNotFound' string
        """
        try:
            with open(self.file_name, "r") as file:
                leader_board = {}
                for line in file.readlines():
                    score, name = line.strip().split(":")
                    leader_board[name] = score
                return leader_board
        except FileNotFoundError:
            with open(self.file_name, "w") as file:
                pass
            return 'FileNotFound'
    
    
    def rewrite_leader_board(self, listed_board):
        """
        Method - writes the updated leaderboard data to a file.
        Parameters:
            listed_board (list): A list of tuples to be written to the file.
        Returns: None
        """
        with open(self.file_name, "w") as file:
            for index, entry in enumerate(listed_board):
                # Not add '\n' when it is the last line
                if index < len(listed_board) - 1:
                    file.write(f"{entry[0]}: {entry[1]}\n")
                else:
                    file.write(f"{entry[0]}: {entry[1]}")

    def update_leaderboard(self, new_score, new_name):
        """
        Method - updates the leaderboard with a new score.
        Parameters:
            new_score (int): The new score to be added to the leaderboard.
            new_name (str): The name associated with the new score.
        Returns: None
        """
        leader_board = self.read_leader_board()
        leader_board = {name: int(score) \
                        for score, name in leader_board.items()}
        if leader_board:
            if new_name in leader_board:
                if int(new_score) < leader_board[new_name]:
                    leader_board[new_name] = int(new_score)
            else:
                leader_board[new_name] = int(new_score)
            sorted_board = sorted(leader_board.items(), 
                                key=lambda item: item[1])
            listed_board = sorted_board[:self.max_entries]
            self.rewrite_leader_board(listed_board)
        else:
            leader_board = {new_name: int(new_score)}
            self.rewrite_leader_board([(int(new_score), new_name)])