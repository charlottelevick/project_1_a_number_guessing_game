"""
Data Analysis Techdegree
Project 1 - A Number Guessing Game
--------------------------------
"""

import random
import sys
from statistics import mean
from statistics import median
from statistics import mode

total_guesses= []

name = input("Hello and welcome to 'The Number Guessing Game! What's your name? ")
user_choice = input("Hi {}! Would you like to play?\n(Please enter y/n) ".format(name))
if user_choice.lower() == "y":
    print("Great! Please choose a number between 1 and 100...")
else:
    print("Ok no worries, see you later {}!".format(name))
    sys.exit()

def start_game():
    number = (random.randint(1,100))
    guess = int(input("Enter your guess: "))
    list_of_guesses = [guess]
    
    while guess != number:
        if (guess > number):
            print("It's lower. Try again: ")
            guess = int(input("Enter your guess: "))
            list_of_guesses.append(guess)
        elif (guess < number):
            print("It's higher. Try again: ")
            guess = int(input("Enter your guess: "))
            list_of_guesses.append(guess)
        elif (guess == number):
            list_of_guesses.append(guess)
            break

    print("Congratulations {}! You got it!".format(name))
   
    guesses_to_win = len(list_of_guesses)
    total_guesses.append(guesses_to_win)
    print("It took you {} time(s) to guess the number {}".format(guesses_to_win, number))

    print("Overall Statistics:")
    saved_attempts_mean = mean(total_guesses)
    print("Mean: {}".format(saved_attempts_mean))
   
    saved_attempts_median = median(total_guesses)
    print("Median: {}".format( saved_attempts_median))
    
    saved_attempts_mode = mode(total_guesses)
    print("Mode: {}".format(saved_attempts_mode))

    restart = input("Want to play again?\n(Please enter y/n)")
    if restart.lower() == "y":
        start_game()
    else:
        print("Ok no worries, see you later {}!".format(name))
        sys.exit()

start_game()