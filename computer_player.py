"""
computer_player.py

Defines an AI-controlled player (from a Player base class) for Hexapawn.

NOTES:
    need to add a way for the AI to remember the moves made during the game (update MENACE)
"""

from player import Player

class ComputerPlayer(Player):
    """
    An AI-controlled player.
    """

    def __init__(self, name, strategy):
        super().__init__(name)
        self.strategy = strategy


    def get_move(self, board):
        """
        Gets an AI's selected move.

        Args:
            board (Board): The game state.

        Returns:
            move (tuple): The move to make as a tuple of (row, column) tuples.
        """
        try:
            move = self.strategy.get_move(board)

            if not isinstance(move, tuple) or len(move) != 2:
                raise ValueError("Move must be a tuple of two board positions in (from location, to location) format.")

            for position in move:
                if not isinstance(position, tuple) or len(position) != 2:
                    raise ValueError("Positions must be a tuple of a board row and column in (row, column) format.")

                if not all(isinstance(element, int) for element in position):
                    raise ValueError("Row and column elements must be integers.")

            return move

        except ValueError:
            print("Invalid move format. Quitting.")