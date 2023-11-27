"""

"""
from get_player_name import get_player_name

def update_player_list():
    """
    store all the winner's name and their scores
    """
    with open('playerlist.txt', 'a') as player_file:
        new_player_score = get_player_score()
        new_player_name = get_player_name()
        
        # Store 2 columns: score, name.
        for rank, lines in enumerate(player_file):

            lines = lines.strip('\n').split()
            score, name = lines[0], lines[1]
            
            
        player_file.write(f"{new_player_score},{new_player_name}\n")

        

def update_leaderboard():
    """
    rank the first 3 players by their scores and 
    """
    pass