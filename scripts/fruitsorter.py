#Buddy Collins
#Network Programming
#Lab 4 Fruit sorter

'''This code will answer the two prompts 1. Write an app that asks the user for 3 fruits. 
Add them to a list, sort them, and print them using a for-loop
Research the thousands of ways to determine if a word is a palindrome using Python. 
Implement one and in addition to the splicing trick on slide 19, use both methods to check if a user-entered string is a palindrome.'''

#!/usr/bin/env python3

shopList = []
print("\nI would like to try 3 fruits \n")
for i in range(1,4):
    fruit = input(f"Enter your number {i} recommendation for fruit: ")
    shopList.append(fruit.lower()) #takes the input and adds it to the list created earlier and lowercase    
    if i == 3:
        shopList.sort()
        print(f"Your chosen fruits in alphabetical order are: {shopList[0]}, {shopList[1]}, {shopList[2]}")

#palindrome tester
pal = input("\nNow enter a palindrome: ").lower()
if pal == ''.join(reversed(pal)).lower(): #https://www.geeksforgeeks.org/python/python-program-check-string-palindrome-not/
    if pal == pal[::-1]: # from the slides
        print(f"\n{pal} is a palindrome. \n")
else:
    print (f"\n{pal} is not a palindrome. \n")

