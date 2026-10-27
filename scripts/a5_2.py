#!/usr/bin/env python

import random,argparse

def ArgParse_slides():
    parser = argparse.ArgumentParser(description="This script will 'roll' the dice for the user, they only need to enter the number of dice and the number of sides the dice have")
    parser.add_argument("numDice",action='store', help="Enter the number of dice in the first position")
    parser.add_argument("numSide",action='store', help="Enter the number of sides for the dice in the second position")
    parser.add_argument("--version",action='version', version='1.2')
    args=parser.parse_args()
    return args

def diceroll(dice,sides):
    roll=0
    for i in range(dice):
        roll += random.randint(1,sides)
    #give an output if the dice min/max values
    if roll == dice:
        return(f"Critical failure! {roll}") 
    elif roll == dice*sides:
        return(f"Critical sucess! {roll}")
    else:
        return(f"You rolled: {roll}")

def main():
    args=ArgParse_slides() # call argparse slides 
    dice = int(args.numDice) # make variables an integer
    sides = int(args.numSide)
    if dice == 0: 
        print("You can't roll without dice...")
        exit()
    if sides < 2:
        print("That's not a dice...")
        exit()
    result = diceroll(dice,sides)
    print(result)

if __name__ == "__main__":
    main()