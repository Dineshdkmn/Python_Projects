# Hangman Game

This is a simple Hangman game implemented in Python.

## Overview

Hangman is a classic word-guessing game where players try to guess a hidden word one letter at a time. For each incorrect guess, a part of the hangman is drawn until the player either guesses the word correctly or runs out of attempts.

## How to Play

1. Run the `main.py` file to start the game.
2. The game will randomly select a word from a predefined list of words embedded in the code.
3. Guess letters one by one to try to uncover the hidden word.
4. You have a limited number of incorrect guesses before the game ends.
5. If you guess all the letters correctly before running out of guesses, you win!

## Features

- Random word selection: Words are randomly selected from a predefined list embedded in the `main.py` file.
- Displaying progress: The game displays the current state of the word, showing correctly guessed letters and placeholders for unknown letters.
- Lives system: Players have a limited number of incorrect guesses before losing the game.
- Input validation: The game validates user input to ensure it is a single letter and hasn't been guessed before.

## Installation

1. Clone or download this repository.
2. Make sure you have Python installed on your system.
3. Run `main.py` using Python to start the game.

## File Structure

- `main.py`: Contains the main code for the Hangman game, including the predefined list of words.

## Contributing

Contributions are welcome! If you have any suggestions, bug reports, or enhancements, feel free to open an issue or submit a pull request.
