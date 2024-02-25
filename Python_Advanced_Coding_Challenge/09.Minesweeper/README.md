# Minesweeper Game

This Python program implements a simple command-line version of the classic Minesweeper game. Players can specify the dimension size of the board and the number of bombs. The objective is to reveal all the safe cells without detonating any bombs.

## How to Play

### Setup:

1. Enter the dimension size of the board.
2. Specify the number of bombs.

### Gameplay:

- Players choose a cell to dig by inputting the row and column separated by a comma.
- The game reveals the contents of the selected cell.
- If the cell contains a bomb, the game ends.
- If the cell is safe, the game continues.
- Players win by revealing all safe cells.

## Features

- Dynamic board creation based on user-defined dimension size and number of bombs.
- Recursive revealing of adjacent safe cells when a safe cell with no neighboring bombs is revealed.
- Display of the number of bombs left to find.
- Automatic game-over when a bomb is revealed, with all bombs displayed.
- Victory message when all safe cells are revealed.

## How to Run

1. Ensure you have Python installed on your system.
2. Clone or download the `main.py` file.
3. Run the script using Python by executing `python3 main.py` in your terminal.

## Contributors

This program was created by mueez. Contributions and improvements are welcome.

