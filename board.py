"""
board.py

Defines a structure for a Hexapawn game board.
"""
import copy


class Board:
    """
    A Hexapawn board state.
    """

    def __init__(self, size=3, state=None):
        """
        Constructor.

        Args:
            size (int): The size of the board (number of rows or columns).
            state (string): A string representing the board state.
        """
        if state is not None:
            if len(list(state)) != (size*size):
                raise ValueError(f'Board state string must have {size}x{size} elements.')
            self.size = size
            self.grid = self.to_matrix(state)
        else:
            self.size = size
            self.grid = self._init_grid()


    def _init_grid(self):
        """
        Sets up the board for a new game.

        None = empty square
        1 = player 1 piece
        2 = player 2 piece

        Returns:
            grid (list): A 2D array that represents the squares of the game board.
        """
        grid = [[None] * self.size for _ in range(self.size)]

        for col in range(self.size):
            grid[0][col] = 2
            grid[self.size-1][col] = 1

        return grid


    def is_valid_position(self, position):
        """
        Checks to make sure a position is within the board space.

        Args:
            position (tuple): A (row, column) tuple.

        Returns:
            (bool): Truth of if the position is within the board space.
        """
        row, col = position
        return 0 <= row < self.size and 0 <= col < self.size


    def get_piece(self, position):
        """
        Gets the game player game piece located at the given position.

        Args:
            position (tuple): The board position as a (row, column) tuple.

        Returns:
            piece: The player game piece.
        """
        row, col = position
        piece = self.grid[row][col]
        return piece


    def get_player_positions(self, player_idx):
        """
        Gets all the locations of pieces the given player has on the board.

        Args:
            player_idx (int): The player index.

        Returns:
            positions (list): A list of (row, col) tuples where the pieces are located.
        """
        player = player_idx + 1 # convert from player index to player number

        positions = []
        for row in range(self.size):
            for col in range(self.size):
                if self.grid[row][col] == player:
                    positions.append((row, col))

        return positions


    def _set_piece(self, piece, position):
        """
        Sets the game player game piece at the given position.

        Args:
            piece: The player game piece.
            position (tuple): The board position as a (row, column) tuple.
        """
        row, col = position
        self.grid[row][col] = piece


    def move_piece(self, from_pos, to_pos):
        """
        Moves a player game piece from the current given position to a new given position.

        Args:
            from_pos (tuple): The (row, column) tuple of the player game piece to move.
            to_pos (tuple): The (row, column) tuple of selected position to move the piece to.
        """
        if self.is_valid_position(from_pos) and self.is_valid_position(to_pos):
            self._set_piece(self.get_piece(from_pos), to_pos)
            self._set_piece(None, from_pos)


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

        piece_positions = self.get_player_positions(player_idx)

        player_direction = -1 if player_idx == 0 else 1 # adjusts move directions to that player's perspective
        opponent_piece = 2 if player_idx == 0 else 1

        for piece_position in piece_positions:
            row, col = piece_position

            diag_left = (row + player_direction, col + player_direction)
            forward = (row + player_direction, col)
            diag_right = (row + player_direction, col - player_direction)

            if self.is_valid_position(diag_left) and self.get_piece(diag_left) == opponent_piece:
                legal_moves.append((piece_position, diag_left))
            if self.is_valid_position(forward) and self.get_piece(forward) is None:
                legal_moves.append((piece_position, forward))
            if self.is_valid_position(diag_right) and self.get_piece(diag_right) == opponent_piece:
                legal_moves.append((piece_position, diag_right))

        return legal_moves


    def copy(self):
        return copy.deepcopy(self)


    def to_string(self):
        """
        Converts the board to a string representation where the beginning
        of the string is the top left of the board and the end of the
        string is the bottom right of the board.

        0 = empty square
        1 = player 1
        2 = player 2

        Returns:
             (string): A compact string representation of the board.
        """
        result = []
        for row in self.grid:
            for square in row:
                result.append(square if square is not None else '0')
        return ''.join(result)


    def to_matrix(self, state):
        """
        Converts a string representation of the board into a matrix.

        Args:
            state (str): A string representation of the board.

        Returns:
            board (list): A matrix representation of the board.
        """
        chars = list(state)
        board = [chars[i:i+self.size] for i in range(0, len(chars), self.size)]

        for r in range(self.size):
            for c in range(self.size):
                if board[r][c] == '0':
                    board[r][c] = None
                elif board[r][c] in ('1', '2'):
                    board[r][c] = int(board[r][c])
        return board


    def __str__(self):
        """

        Returns:
            (string): A graphical string representation of the board.
        """
        result = []

        # column headers
        result.append('   ')
        for col in range(self.size):
            result.append(f'  {col}')
        result.append('\n')
        result.append('     -  -  -\n')

        # row headers and board
        for row in range(self.size):
            result.append(f'{row} | ')
            for col in range(self.size):
                square = self.grid[row][col] if self.grid[row][col] is not None else '0'
                result.append(f' {square} ')
            result.append('\n')

        return ''.join(result)