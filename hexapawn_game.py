"""
hexapawn_game.py

Defines a controller that manages a Hexapawn game.

NOTES:
    consider passing the legal moves and player position to agent on each move
    remove console output when there are two ComputerPlayers playing
"""

from board import Board
from player import Player
from computer_player import ComputerPlayer

class HexapawnGame:
    """
    Manages a hexapawn game.

    Contains game logic, facilitates moves between players, and
    checks for a win.
    """

    def __init__(self, player_1, player_2, board=None, start_player=None):
        self.players = [player_1, player_2]
        self.game_history = []                               # list of (board, move) tuples, board is a string, move is a tuple of int tuples
        self.board = board if board is not None else Board() # set up a new board if necessary
        self.current_player_idx = 0 if start_player is None else start_player - 1 # the position of the current player (start with player 1)
        self.is_game_over = False
        self.winner_idx = None                               # the position of who won


    def next_player_turn(self):
        """
        Advances game play to next player.
        """
        self.current_player_idx = 1 if self.current_player_idx == 0 else 0


    def check_game_over(self):
        """
        Checks for game over conditions.

        Game is over if:
            - the player has a promoted pawn
                            or
            - the opponent is left with no legal moves
        """
        promotion = False
        for piece_position in self.board.get_player_positions(self.current_player_idx+1):
            row, _ = piece_position
            if self.current_player_idx == 0 and row == 0:
                promotion = True
            if self.current_player_idx == 1 and row == self.board.size-1:
                promotion = True

        next_player_idx = 1 if self.current_player_idx == 0 else 1
        no_legal_moves = (len(self.board.get_legal_moves(next_player_idx)) == 0)

        if promotion or no_legal_moves:
            self.is_game_over = True
            self.winner_idx = 0 if self.current_player_idx == 0 else 1


    def make_move(self, from_pos, to_pos):
        """
        Makes a player's selected move if legal.

        Args:
            from_pos (tuple): A tuple of (row, col) positions where the piece is.
            to_pos (tuple): A tuple of (row, col) positions where the piece is to move to.

        Returns:
            (bool): The truth of whether the move was made or not.
        """
        legal_moves = self.board.get_legal_moves(self.current_player_idx+1)
        move = (from_pos, to_pos)

        if move in legal_moves:
            self.board.move_piece(from_pos, to_pos)
            return True
        else:
            return False


    def send_report(self):
        """
        Outputs the results of the game. Calls the game_report function for
        computer players. Prints game results.
        """
        for index, player in enumerate(self.players):
            if isinstance(player, ComputerPlayer):
                player_position = index + 1
                winner_position = self.winner_idx + 1
                player.game_report(self.game_history, player_position, winner_position)

        print(self.board)
        print(f'Game over! {self.players[self.winner_idx].name} wins!')


    def play(self):
        """
        Manages game play loop.
        """
        while not self.is_game_over:

            print(self.board)
            print(f'{self.players[self.current_player_idx].name}\'s turn.')

            selected_move = None
            legal_moves = self.board.get_legal_moves(self.current_player_idx+1)

            loop_count = 0
            while selected_move not in legal_moves and loop_count < 10:
                selected_move = self.players[self.current_player_idx].get_move(self.board.to_string())

                if selected_move is None:
                    print('Quitting...')
                    quit()

                from_pos, to_pos = selected_move
                last_board = self.board.copy() # current board, but is about to be last board-- we need a copy before the move is made

                if self.make_move(from_pos, to_pos):
                    self.game_history.append( (last_board.to_string(), selected_move) )
                    print(f'Moved {self.players[self.current_player_idx].name}\'s piece from {from_pos} to {to_pos}.\n')
                else:
                    print('Move not legal!')

                loop_count += 1

            self.check_game_over()
            self.next_player_turn()

        self.send_report()