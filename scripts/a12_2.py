#!/usr/bin/env python

from random import randint


class hotdog:
    def __init__(self):
        self.dog = "100% beef frank"
        self.bun = "plain"
        self.toppings = []
        self.speciality = "nothing special"

    # I wanted to try to add to a list cause I feel like this could help in the future
    def additions(self, added):
        if added:
            self.toppings.append(added)
            print(f"Plus one {added}")
        else:
            print("nothing added")
            return 0

    # if the dog has intrinsic value or not
    def special(self):
        self.speciality = "a very special dog"

    # sometimes life gives you a stale bun
    def staleBun(self):
        self.bun = "stale"

    # string output
    def __str__(self):
        return f"hotdog is a {self.dog} with a {self.bun} bun and {self.toppings}. It's {self.speciality}"


def main():
    # define the hotdog var
    dog = hotdog()
    # loop to add ingredients to the hotdog used while true cause I couldn't find a good way to use an imcrement or a int value test
    while True:
        addition = input(f"what would you like to add to your {dog.dog}? ")
        # breaks the loop if nothing is entered
        if addition == "":
            break
        dog.additions(addition)

    # if the dog is special, I could expand here
    special = input(f"Is this a special dog? ")
    # true false if the dog is special
    if special:
        dog.special()

    # rolls to decide if you get a stale bun or not for fun
    rng = randint(1, 2)
    if rng == 2:
        dog.staleBun()
    print(dog)


if __name__ == "__main__":
    main()
