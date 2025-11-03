# Hexapawn

### Project Overview
Inspired by Donald Michie’s [MENACE](https://en.wikipedia.org/wiki/Matchbox_Educable_Noughts_and_Crosses_Engine) reinforcement learning experiment, this project provides a simple Hexapawn environment for experimenting with decision-making and learning algorithms.

<!-- 
![Python](https://img.shields.io/badge/python-3.10+-blue)
![License](https://img.shields.io/badge/license-MIT-green)


### Project Info
```
Author:      T. Stratton
Start Date:  1-NOV-2025
```
-->

<p align="center">
  <img src="hexapawn_board.png" alt="Hexapawn board setup" width="300"/>
</p>

### Gameplay

[Hexapawn](https://en.wikipedia.org/wiki/Hexapawn) is a two-player deterministic, zero-sum strategy game. Invented by Martin Gardner, it is a simplified version of Chess. Two players face off on a 3x3 board with only 3 pawns each.

In a turn, a pawn may be moved forward one square (if that square is empty) or diagonally forward one square if that square is occupied by an enemy pawn (a capture).

The game is won when a pawn reaches the opposite side (promotion) or the opponent has no legal moves remaining.


### Features
- supports human v. human, human v. AI, and AI v. AI gameplay
- flexible API for integrating user-supplied AI agents
- terminal-based interface for display and gameplay (for human gameplay)
- modular board size, allowing for play of Octopawn (or larger Hexapawn derivatives)

### Future Features
- GUI - improved visualization

---

## API

### Board Representation
- The board is represented as a row-major 2D array where (row, col) indexes start at (0,0) in the top-left corner from Player 1’s perspective. 
- A string representation is used by flattening the 2D array into a single string of 9 characters (for a 3×3 board), with (0,0) appearing first. 
- Values in the representation:
  - 0 → empty square

  - 1 → Player 1’s pawn

  - 2 → Player 2’s pawn

- Example: The board shown in the image above would be represented as:
222000111

### Player Class
`Player(name: str, filepath: str)`

- **Description**: Represents a player in the Hexapawn environment.
- **Constructor Arguments**:
  - `name` (`str`): The name of the player.
  - `filepath` (`str`): Path to the agent class implementation.

### Agent Interface
- Any agent used with `Player` must implement a `get_move(board_state: str)` method.
  ```python
  get_move(board_state: str) -> ((from_row, from_col), (to_row, to_col))
- Arguments:
  - board_state (str): Flattened string representation of the board (see Board Representation above)
- Returns:
  - A tuple of two coordinates indicating the move: ((from_row, from_col), (to_row, to_col))

NOTE: Future versions may include legal moves (as a list) as an additional argument to `get_move`.