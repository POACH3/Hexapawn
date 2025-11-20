"""
computer_player.py

Defines an AI-controlled player (from a Player base class) for Hexapawn.

NOTES:
    none
"""

from player import Player

class ComputerPlayer(Player):
    """
    An AI-controlled player.
    """

    def __init__(self, name, agent):
        """
        Constructor.

        Args:
            name (str): The name of the player.
            agent: An instance of the AI class whose logic controls the player.
        """
        super().__init__(name)
        self.agent = agent


    def get_move(self, board):
        """
        Gets an agent's selected move.

        Args:
            board (Board): The game state.

        Returns:
            move (tuple): The move to make as a tuple of (row, column) tuples.
        """
        try:
            move = self.agent.get_move(board)

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


    def game_report(self, game_history, player_position, winner_position):
        """
        Provides feedback to the agent.

        Args:
            game_history (list): The game history represented as a list of (state, move) tuples .
            player_position (int): The player number of the player receiving this report.
            winner_position (int): The player number of the winner.
        """
        self.agent.game_report(game_history, player_position, winner_position)