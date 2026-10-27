#!/usr/bin/env python

import argparse
from random import randint

def ArgParse_slides():
    parser = argparse.ArgumentParser(description="Script takes two lists and joins them to create a dictionary")
    parser.add_argument("--version",action='version', version='1.3')
    args=parser.parse_args()
    return args

def main():
    valueList = []
    keyList = ["Pear","Apple","Orange","Watermelon","Banana","Tomato"]
    fruitInv = {} # makes a dictionary
    k = 0 #int var to iterate second list

    #this loop joins the two lists using what I learned from geeksforgeeks
    for i in keyList:
        valueList.append(randint(0,50)) # assign a random number for the item amount
        fruitInv[i] = valueList[k] # this looks odd but I guess it works! https://www.geeksforgeeks.org/python/python-dictionary/
        k+=1
    #key for loop I know I can do both at once but the output looks bad
    for key in fruitInv.keys():
        print(f"Here are the keys: {key}")
    #value for loop
    for value in fruitInv.values():
        print(f"Here are the values: {value}")

    print(f"Here is the whole dictionary {fruitInv}")

#namespace check
if __name__ == "__main__":
    main()