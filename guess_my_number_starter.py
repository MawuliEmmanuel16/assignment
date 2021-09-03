"""
File: guessmynumber.py
----------------------
This program checks if a user's guess of a number matches that guessed by the computer
"""

import random
# use code below  to generate a random integer between 30 and 50 for example
print(random.randint(30, 50))

# ********************************** YOUR CODE GOES BELOW HERE *********************************************************

name = input("Hello, What is your name? ")
# this function asks the user to enter the name. this function only takes names in the form of a string
print("hello," + name)
print(name + " You are welcome to the game of guesses")
print("I am thinking of a number, can you guess it?, go ahead and give it a try")
while True:
    # this function tells python to continue executing a statement if the condition is true.(in this case,
    # if the secret number is equal to the guess)
    Guess = int(input("Enter your guess: "))
    # the user is made to guess a figure which should be in the form of an integer. the guess is stored with the
    # variable name "guess"
    secret_number = random.randint(1, 99)
    # this code gives a random number which must be an integer
    if Guess > secret_number:
        print(name + " Sorry!, Your guess is too high. Please Try Again")
    # this prints out an error message if the guess is lower than the secret number.
    elif Guess < secret_number:
        print(name + " Sorry!, Your guess is too low. Please Try again")
    # an error code prints again if the guess is too high
    elif Guess == secret_number:
        print("Congratulations!!, You guessed right. You are a true genius " + name)
        break
# this elif statement prints if the guess is equal to the secret number, the user receives a congratulatory message.
# the break statement breaks or stops the execution of the while function if the secret number equals the guess made.


