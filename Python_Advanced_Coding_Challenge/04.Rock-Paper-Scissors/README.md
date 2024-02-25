# Rock, Paper, Scissors Game

This is a simple Python implementation of the classic Rock, Paper, Scissors game where the user plays against the computer.

## How to Play

1. Run the `play()` function.
2. You will be prompted to enter your choice: 'r' for rock, 'p' for paper, or 's' for scissors.
3. The computer will randomly choose one of the options.
4. The winner is determined based on the following rules:
   - Rock beats scissors
   - Scissors beats paper
   - Paper beats rock
5. The game result (win, lose, or tie) will be displayed.

## How to Run

1. Make sure you have Python installed on your system.
2. Copy the code provided into a Python file (e.g., `main.py`).
3. Run the Python file in your terminal or command prompt by typing `python main.py` and hitting Enter.

## Code Explanation

- The `play()` function handles the game's main logic, including user input, computer choice, and result determination.
- The `is_win(player, opponent)` function checks the winning conditions based on the player's choice and the opponent's choice.
- The program uses the `random` module to generate the computer's choice randomly.
