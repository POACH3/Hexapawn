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
            return move

        except ValueError:
            print("Invalid move format. Quitting.")