import random
import string

def get_valid_word(word_list):
    word = random.choice(word_list)
    while '_' in word or ' ' in word:
        word = random.choice(word_list)
    return word

def display_word(word, guessed_letters):
    return ' '.join([letter if letter in guessed_letters else '_' for letter in word])

def hangman():
    words = ["PYTHON", "JAVA", "RUBY", "PHP", "JAVASCRIPT", "CSS", "HTML", "KOTLIN"]
    word = get_valid_word(words)
    word_characters = set(word.upper())
    guessed_letters = set()
    lives = 6

    print("Welcome to Hangman!")
    print("You have 6 lives to guess the word.")
    print(display_word(word, guessed_letters))

    while word_characters and lives > 0:
        user_input = input("Guess a letter: ").upper()

        if user_input.isalpha() and len(user_input) == 1:
            if user_input in guessed_letters:
                print("You have already guessed that letter. Please try again.")
            elif user_input in word_characters:
                guessed_letters.add(user_input)
                print("Correct guess!")
                print(display_word(word, guessed_letters))
            else:
                guessed_letters.add(user_input)
                lives -= 1
                print("Incorrect guess.")
                print("You have", lives, "lives left.")
                print(display_word(word, guessed_letters))
        else:
            print("Invalid input. Please enter a single letter.")

    if lives == 0:
        print("Sorry, you ran out of lives. The word was:", word)
    else:
        print("Congratulations, you guessed the word:", word)

hangman()
