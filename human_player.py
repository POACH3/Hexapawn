"""
human_player.py

Defines a human-controlled player (from a Player base class) for Hexapawn.
"""

from player import Player

class HumanPlayer(Player):
    """
    A human-controlled player.
    """

    def get_move(self, board):
        """
        Gets the player's selected move.
        User input format validation is done here.
        Move legality validation is done by the game controller.

        Args:
            board (Board): The current board state.

        Returns:
            move (tuple): The from (row, col) tuple and to (row, col) tuple.
        """
        while True:
            player_input = input('Enter your move: ')

            try:
                parts = player_input.split(',')

                if parts[0] == 'q':
                    return None

                if len(parts) != 4:
                    raise ValueError

                move = ( (int(parts[0]),int(parts[1])), (int(parts[2]),int(parts[3])) )
                return move

            except ValueError:
                print('Invalid input! Enter four comma separated numbers in this format: ')
                print('  from_row,from_column,to_row,to_column')