#!/usr/bin/env python

import a6_2a

def main():
    args=a6_2a.ArgParse_slides() # call argparse slides funciton from other file
    print("Hello there")
    print(f"General {args.username}")

if __name__ == "__main__":
    main()