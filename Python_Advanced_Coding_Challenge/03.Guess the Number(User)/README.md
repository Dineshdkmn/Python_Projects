# Computer Guessing Game

This Python program is a guessing game where the computer tries to guess a number that the user has chosen within a specified range.

## How to Play

1. Run the computer_guess(x) function, where x is the maximum number allowed in the range.
2. Think of a number between 1 and x, inclusive.
3. The computer will start guessing numbers within this range and prompt you to provide feedback on each guess.
4. If the computer's guess is too high, type 'H'. If it's too low, type 'L'. If it's correct, type 'C'.
5. The game continues until the computer guesses the correct number.
6. Once the computer guesses the number correctly, the program will display a congratulatory message.

## About the Program

- The program uses the random module in Python to generate random numbers for the computer's guesses.
- It employs a binary search algorithm to efficiently narrow down the search range based on the user's feedback.
- The computer_guess(x) function takes an argument x, which specifies the maximum number allowed in the range of possible guesses.
- Feedback from the user ('H', 'L', or 'C') is used to adjust the range of possible guesses for the computer.
- The program ensures that the guessing range remains valid and handles cases where the range becomes empty.

## How to Run

1. Make sure you have Python installed on your system.
2. Copy the code provided into a Python file (e.g., main.py).
3. Run the Python file in your terminal or command prompt by typing python main.py and hitting Enter.