import random

def guess(x):
    random_nmbr = random.randint(1, x)
    guess = 0
    while guess != random_nmbr:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if guess < random_nmbr:
            print('Sorry, guess again. The number is too low.')
        elif guess > random_nmbr:
            print('Sorry, guess again. The number is too high.')
    print(f'Yay, congrats. You have guessed the number {random_nmbr}correctly!!')
guess(7)