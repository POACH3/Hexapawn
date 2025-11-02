"""
player.py

Defines an abstract player class.
"""

class Player:
    """
    Defines the base class for all players.
    """

    def __init__(self, name):
        self.name = name

    def get_move(self, board):
        """
        Gets a move to make from the player.

        Args:
            board (Board): The board state

        Returns:
            move (tuple): The move to make as a tuple of (row, column) tuples.
        """
        raise NotImplementedError('Subclasses must implement a get_move() method.')