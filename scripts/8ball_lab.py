
#                   _
#                  /^\   / -- )
#                 / | \ (____/
#                / | | \ / /
#               /_|_|_|_/ /
#                |     / /
# __    __    __ |    / /__    __    __
#[  ]__[  ]__[  ].   / /[  ]__[  ]__[  ]
#|__            ____/ /___           __|
#   |          / .------  )         |
#   |         / /        /          |
#   |        / /        /           |
#~~~~~~~~~~~~------------~~~~~~~~~~~~~~~~~~
#Artist: Unknown


'''This script will mimic a magic 8-ball to that it will print two lines to the screen. 
One being the intro and the second being the fortune I use. 
The randrange to produce an integer within a range that I can use as an index for my list. 
I then print the string at the chosen index.
I also included a fun module.'''

#!/usr/bin/env python3
#Not sure how this works yet

from random import randrange

print("\nYou shake the 8-ball")
list1 = ["it might be so","as I see it, maybe", 
         "could be likely", "maybe, no or maybe, yes", 
         "is random actually random?","you could ask again later", 
         "my reply is uncertain", "my sources say might be negative"]
print(f"The ball responds {list1[randrange(0,9)]}\n") 
#randrange gives me an integer in that range and with it inside the brackets of list1 that means it indexes the list.

#import this


#import "this" is a module that prints out the python words to live by. By Tim Peters
#Source https://github.com/orkohunter/python-easter-eggs

