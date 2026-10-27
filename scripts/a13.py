#!/usr/bin/env python

import argparse
from time import sleep


def ArgParse_slides():
    parser = argparse.ArgumentParser(
        description="This script will create a doubly linked list and print forward and print backwards"
    )

    parser.add_argument("--version", action="version", version="1.8")
    args = parser.parse_args()
    return args


# create the class of songs cause it seems like one of the usecases for doubly linked lists is a playlist
class songs:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.last = None


def main():
    # define the vars with the classes
    song1 = songs("Mr. Brightside")
    song2 = songs("Dancing Queen")
    song3 = songs("Uptown Funk")
    song4 = songs("Choosing Texas")
    song5 = songs("Boston")
    # build the list for navigation
    song1.next = song2
    song1.last = song5
    song2.next = song3
    song2.last = song1
    song3.next = song4
    song3.last = song2
    song4.next = song5
    song4.last = song3
    song5.next = song1
    song5.last = song4

    # I think that a while loop was the best way to navigate the list with user input in mind
    iterator = song1
    while iterator:
        print(f"Playing {iterator.value}")
        choice = input(
            f"Continue with next song? next/replay/last or enter to exit  "
        ).lower()
        if choice == "next":
            iterator = iterator.next
        elif choice == "replay":
            print("Again? okay")
        elif choice == "last":
            iterator = iterator.last
        elif choice == "":  # breaks the loop with an enter key
            break
        else:
            print("err try again")


if __name__ == "__main__":
    main()
