#!/usr/bin/env python

from datetime import datetime
from time import sleep

def timeReturner():
    return datetime.now() 
#I noticed I can just print this out with a void function from the slides

def usrYayNay(usrIn): # I think this may come in handy this semester
    usrIn = input("Would you like to continue y/n? ").lower()
    if usrIn not in ["y","n","yes","no"]: #sometimes I make mistakes so at least one catch
        print("Invalid input please try again.")
        usrIn = input("Would you like to continue y/n? ").lower()
        if usrIn not in ["y","n","yes","no"]: # graceful exit
            print("Invalid input exiting program")
            usrIn = "n"
            return usrIn # returns n
    if usrIn == "n" or usrIn == "no": 
        print("Exiting program")
        return usrIn #returns n or no
    return usrIn # returns y or yes

def main():
    usrIn = "y" #starts the while loop
    while usrIn == "y" or usrIn == "yes": 
        print(f"The time is {timeReturner()}. Starting 30 second time out.")#calls my function in the f print
        sleep(30) #30 seconds is a long time
        print(f"Waiting is complete. Current time is {timeReturner()}.") 
        usrIn = usrYayNay(usrIn) #calls my function
if __name__ == "__main__":
    main()