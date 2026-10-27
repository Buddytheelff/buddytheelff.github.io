#!/usr/bin/env python
import argparse

def ArgParse_slides():
    parser = argparse.ArgumentParser(description="I am not sure how useful this will be in a separate file")
    parser.add_argument("username",action='store', help="user enters name")
    parser.add_argument("--version",action='version', version='1.2')
    args=parser.parse_args()
    return args

def main():
    args=ArgParse_slides() # call argparse slides 
    print(f"hello {args.username}") # I wanted to include a main 

if __name__ == "__main__":
    main()