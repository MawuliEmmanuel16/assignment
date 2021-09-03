"""
File: khansole_academy.py
-------------------------
Khansole Academy is a program that teaches users how to add by asking users to input answers for the addition of two
randomly generating integers between 10 and 99 inclusive. The program returns feedback based on the User's answers.

"""

import random
# use code below  to generate a random integer between 30 and 50 for example
print(random.randint(30, 50))

# ********************************** YOUR CODE GOES BELOW HERE *********************************************************
guess_attempt = 1
# this represents the number of attempts the user has.
while guess_attempt <= 3:
    # this executes the loop continuously until the condition is met and the attempts is up. the user keeps adding
    # until he scores three attempts correctly
    first_number = random.randint(10, 99)
    # this code picks up a random integer within the range of 10 and 99 and assigns it the variable name.
    second_number = random.randint(10, 99)
    # the cde also guesses a random integer within the range of 10 and 99
    correct_answer = first_number + second_number
    # the code calculates the correct answer and stores it in memory.
    print("what is", first_number, "+", second_number)
    Answer = input("Your Answer: ")
    # the user is asked a question which an answer is required before the execution continues.
    if Answer == correct_answer:
        guess_attempt += 1
        print("Correct!. You have gotten", guess_attempt, "correct in a row")
        print("Congratulations!, You made it. You now have a certificate in addition.")
        # if the user's answer is correct the user is given opportunity to answer two more attempts after which a
        # congratulatory message is printed if they are all correct
    else:
        print("Incorrect!, the correct answer is", correct_answer)
        guess_attempt = 1
        # the else statement prints when the answer is not correct and the user is made to answer another question.
        # the guess attempt =1 is the indexing variable that repeats the question if the answer is wrong






