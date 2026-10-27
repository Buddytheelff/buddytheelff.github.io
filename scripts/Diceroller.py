#!/usr/bin/env python3


'''
2. Complete practice problem #2 & #3 and upgrade it to use argparse. 
Make it so that the user supplies the number of dice to roll and the number of sides as 2 arguments. 
Include a help message/version info.

Dnd uses a 20 sided dice to play. simulate the die being rolled.
indicate a critical role if a 1 or 20 is rolled.

practice problem 2 update dice roller app to be a function.
The function should take the number of dic to roll and
the number of sides as arguments and return the roll.
'''

from random import randint
import argparse

def ArgParse_slides():
    parser = argparse.ArgumentParser(description="This script will 'roll' the dice for the user, they only need to enter the number of dice and the number of sides the dice have")
    parser.add_argument("numDice",action='store', help="Enter the number of dice in the first position")
    parser.add_argument("numSide",action='store', help="Enter the number of sides for the dice in the second position")
    parser.add_argument("--version",action='version', version='1.1')
    args=parser.parse_args()
    return args
args=ArgParse_slides()


numDice = int(args.numDice) # int checker/converter function could use len() to find length of a string or kick the user out
numSide = int(args.numSide)

print(f"you have decided to roll {numDice} dice.")
print(f"you have chosen {numSide} sides.")

diceLS = []
while numDice > 0:
    diceLS.append(randint(0,numSide))
    numDice -= 1

for i in diceLS:
    if i == 20:
        print(f"You rolled a {i} Critical Success!")
    elif i == 1:
        print(f"You rolled a {i} Critical Failure!")
    else:
        print(f"You rolled a {i}")

