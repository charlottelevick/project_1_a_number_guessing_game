"""
Data Analysis Techdegree
Project 1 - A Number Guessing Game
--------------------------------
"""

# Import the random and statistics modules.
import random
from statistics import mean
from statistics import median
from statistics import mode

# Create the start_game function.
# Write your code inside this function.
total_guesses= []

name = input("Hello and welcome to 'The Number Guessing Game! What's your name? ")
user_choice = input("Hi {}! Would you like to play?\n(Please enter y/n) ".format(name))
if user_choice.lower() == "y":
    print("Great! Please choose a number between 1 and 100...")
else:
    print("Ok no worries, see you later {}!".format(name))

def start_game():
    #   When the program starts, we want to:
    #   ------------------------------------
    #   1. Display an intro/welcome message to the player.
    #   2. Store a random number as the answer/solution.
    number = (random.randint(1,100))
    guess = int(input("Enter your guess: "))
    list_of_guesses = [guess]
    #   3. Continuously prompt the player for a guess.
    #     a. If the guess is greater than the solution, display to the player "It's lower".
    #     b. If the guess is less than the solution, display to the player "It's higher".
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

    #   4. Once the guess is correct, stop looping, inform the user they "Got it" and store the number of guesses it took in a list.
    print("Congratulations {}! You got it!".format(name))
    #   5. Display the following data to the player
    #     a. How many attempts it took them to get the correct number in this game
    guesses_to_win = len(list_of_guesses)
    total_guesses.append(guesses_to_win)
    print("It took you {} time(s) to guess the number {}".format(guesses_to_win, number))

    #     b. The mean of the saved attempts list
    print("Overall Statistics:")
    saved_attempts_mean = mean(total_guesses)
    print("Mean: {}".format(saved_attempts_mean))
    #     c. The median of the saved attempts list
    saved_attempts_median = median(total_guesses)
    print("Median: {}".format( saved_attempts_median))
    # d. The mode of the saved attempts list
    saved_attempts_mode = mode(total_guesses)
    print("Mode: {}".format(saved_attempts_mode))

#   6. Prompt the player to play again
    restart = input("Want to play again?")
    if user_choice.lower() == "y":
        start_game()
    else:
        print("Ok no worries, see you later {}!".format(name))
#     a. If they decide to play again, start the game loop over.
#     b. If they decide to quit, show them a goodbye message.


# ( You can add more features/enhancements if you'd like to. )


# Kick off the program by calling the start_game function.
start_game()