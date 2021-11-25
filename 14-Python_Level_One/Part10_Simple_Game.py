###########################
## PART 10: Simple Game ###
### --- CODEBREAKER --- ###
## --Nope--Close--Match--##
###########################

# It's time to actually make a simple command line game so put together everything
# you've learned so far about Python. The game goes like this:

# 1. The computer will think of 3 digit number that has no repeating digits.
# 2. You will then guess a 3 digit number
# 3. The computer will then give back clues, the possible clues are:
#
#     Close: You've guessed a correct number but in the wrong position
#     Match: You've guessed a correct number in the correct position
#     Nope: You haven't guess any of the numbers correctly
#
# 4. Based on these clues you will guess again until you break the code with a
#    perfect match!

# There are a few things you will have to discover for yourself for this game!
# Here are some useful hints:

# Try to figure out what this code is doing and how it might be useful to you
import random
from typing import Dict


def random_digits():
    digits = list(range(10))
    random.shuffle(digits)
    return digits[:3]


def number_correct(guess: list, answer: list) -> Dict[str, int]:
    dict = {"inPosition": 0, "inWrongPosition": 0}
    for i in range(3):
        if guess[i] == answer[i]:
            dict["inPosition"] += 1
        elif guess[i] in answer:
            dict["inWrongPosition"] += 1
    return dict


random_number = random_digits()
print(random_number)
user_guess = []

while user_guess != random_number:
    guess = input("What is your guess? ")
    print(guess)
    if len(guess) == 3:
        user_guess.clear()
        user_guess.append(int(guess[0]))
        user_guess.append(int(guess[1]))
        user_guess.append(int(guess[2]))
    else:
        print("Please enter three digits.")
        continue

    if user_guess == random_number:
        print("You guessed the number!")
        break
    else:
        guess_positions = number_correct(user_guess, random_number)

        if guess_positions["inPosition"] == 1:
            print("You've guessed a correct number in the correct position")
        elif guess_positions["inPosition"] > 1:
            print("You've guessed {} correct numbers in the correct position".format(
                  guess_positions["inPosition"]))

        if guess_positions["inWrongPosition"] == 1:
            print("You've guessed a correct number in the wrong position")
        elif guess_positions["inWrongPosition"] > 1:
            print("You've guessed {} correct numbers in the wrong position".format(
                  guess_positions["inWrongPosition"]))

# Think about how you will compare the input to the random number, what format
# should they be in? Maybe some sort of sequence? Watch the Lecture video for more hints!
