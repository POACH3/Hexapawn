from board import Board
from player import Player

class HexapawnGame:
    """
    Manages a hexapawn game.

    Contains game logic, facilitates moves between players, and
    checks for a win.
    """

    def __init__(self, player_1, player_2, board=None):
        self.players = [player_1, player_2]
        self.board = board if board is not None else Board() # set up a new board if necessary
        self.current_player_idx = 0                          # start with player 1
        self.is_game_over = False
        self.winner = None                                   # who won


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
        for piece_position in self.board.get_all_pieces(self.current_player_idx):
            row, _ = piece_position
            if self.current_player_idx == 0 and row == 0:
                promotion = True
            if self.current_player_idx == 1 and row == self.board.size-1:
                promotion = True

        next_player = 1 if self.current_player_idx == 0 else 0
        no_legal_moves = (len(self.get_legal_moves(next_player)) == 0)

        if promotion or no_legal_moves:
            self.is_game_over = True
            self.winner = 0 if self.current_player_idx == 0 else 1


    def get_legal_moves(self, player_idx):
        """
        Gets legal moves available for the given player, given the current board state.

        Legal moves are:
            - in board (within the grid)
            - diagonal left 1 square if occupied by an opponent's piece (capture)
            - forward 1 square if not occupied by an opponent's piece
            - diagonal right 1 square if occupied by an opponent's piece (capture)

        Args:
            player_idx (int): The index of the player whose moves are being checked.

        Returns:
            legal_moves (list): A list of from position --> to position tuples.
        """
        legal_moves = []

        piece_positions = self.board.get_piece_positions(player_idx)

        player_direction = -1 if player_idx == 0 else 1 # adjusts move directions to that player's perspective
        opponent_piece = 2 if player_idx == 1 else 1

        for piece_position in piece_positions:
            row, col = piece_position

            diag_left = (row + player_direction, col + player_direction)
            forward = (row + player_direction, col)
            diag_right = (row + player_direction, col - player_direction)

            if self.board.is_valid_position(diag_left) and self.board.get_piece(diag_left) == opponent_piece:
                legal_moves.append((piece_position, diag_left))
            if self.board.is_valid_position(forward) and self.board.get_piece(forward) is None:
                legal_moves.append((piece_position, forward))
            if self.board.is_valid_position(diag_right) and self.board.get_piece(diag_right) == opponent_piece:
                legal_moves.append((piece_position, diag_right))

        return legal_moves


    def make_move(self, from_pos, to_pos):
        """
        Makes a player's selected move if legal.

        Args:
            from_pos (tuple): A tuple of (row, col) positions where the piece is.
            to_pos (tuple): A tuple of (row, col) positions where the piece is to move to.

        Returns:
            (bool): The truth of whether the move was made or not.
        """
        legal_moves = self.get_legal_moves(self.current_player_idx)
        move = (from_pos, to_pos)

        if move in legal_moves:
            self.board.move_piece(from_pos, to_pos)
            return True
        else:
            return False


    def play(self):
        """
        Manages game play loop.
        """
        while not self.is_game_over:

            print(self.board)
            print(f'{self.players[self.current_player_idx].name}\'s turn.')

            legal_moves = self.get_legal_moves(self.current_player_idx)
            from_pos, to_pos = self.players[self.current_player_idx].get_move(self.board, legal_moves)

            if self.make_move(from_pos, to_pos):
                print(f'Moved from {from_pos} to {to_pos}.')
            else:
                print('Move not legal!')

            self.check_game_over()
            self.next_player_turn()

        print(self.board)
        print('Game over!')
        print(f'Player {self.players[self.winner].name} wins!')