
class Board:
    """
    A structure to represent a Hexapawn board.
    """

    def __init__(self, size=3):
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
                    positions.append(self.grid[row][col])

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


    def copy(self):
        pass


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


    def __str__(self):
        """

        Returns:
            (string): A graphical string representation of the board.
        """
        result = []

        # column headers
        result.append('    ')
        for col in range(self.size):
            result.append(f' {col}')
        result.append('\n')

        # row headers and board
        for row in range(self.size):
            result.append(f'{row} ')
            for col in range(self.size):
                square = self.grid[row][col] if self.grid[row][col] is not None else '0'
                result.append(f' {square}')
            result.append('\n')

        return ''.join(result)