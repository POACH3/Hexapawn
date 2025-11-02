```
Author:      T. Stratton
Start Date:  1-NOV-2025
```

---

# Hexapawn

Inspired by Donald Michie's exploration with MENACE, this little project is merely a means to explore algorithms in a simple environment.

### Game Play

<p align="center">
  <img src="hexapawn_board.png" alt="Hexapawn board setup" width="300"/>
</p>

Hexapawn is a simplified version of Chess. Two players face off on a 3x3 board with only 3 pawns each.

Pawns may move forward one square (if that square is empty) or diagonally forward one square if that square is occupied by an enemy pawn (a capture).

The game is won by the player whose pawn reaches the opposite side of the board (promotion) or they leave their opponent unable to make a legal move.


### Features
- terminal based GUI
- the board size is modular, so Octopawn (or larger Hexapawn derivatives) may be played
- supports human v. human, human v. AI, and AI v. AI game play
- different AI strategies allowed

### Future Functionality
- maybe a better GUI?