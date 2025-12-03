# Sudoku Game in Python

A fully playable command-line Sudoku game with puzzle generation and validation.

## Features

- **4 Difficulty Levels**: Easy, Medium, Hard, and Expert
- **Puzzle Generation**: Creates valid, solvable Sudoku puzzles
- **Input Validation**: Checks if moves follow Sudoku rules
- **Hint System**: Get hints when stuck
- **Solution Viewer**: View the complete solution
- **Reset Function**: Start over with the same puzzle

## How to Play

1. Run the game:
```bash
python3 sudoku.py
```

2. Select difficulty level (1-4)

3. Game commands:
   - **Make a move**: `row col number` (e.g., `1 1 5` places 5 at row 1, column 1)
   - **Get a hint**: Type `hint`
   - **See solution**: Type `solve`
   - **Reset puzzle**: Type `reset`
   - **Quit game**: Type `quit`

## Game Rules

- Fill the 9×9 grid with numbers 1-9
- Each row must contain all digits 1-9
- Each column must contain all digits 1-9
- Each 3×3 box must contain all digits 1-9
- You cannot change the pre-filled numbers

## Example Session

```
Select difficulty:
1. Easy
2. Medium
3. Hard
4. Expert

Enter choice (1-4, default is 2): 2

    1  2  3  4  5  6  7  8  9
  +---+---+---+---+---+---+---+---+---+
1 | 5 3 4 | . . . | 9 . . |
2 | . 2 . | 8 . . | 4 . 6 |
3 | . 8 9 | . 7 . | 2 . . |
  +---+---+---+---+---+---+---+---+---+
...

Enter your move: 1 4 6
```

Enjoy playing Sudoku!
