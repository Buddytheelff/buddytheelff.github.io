#!/usr/bin/env python

# Black formatter: shift + alt + F
import argparse

class Server:
    def __init__(self, Name, IP):
        self.Name = Name
        self.IP = IP
    def ping(self, IP):
        return f"{IP} \nPing function coming soon"
    
def ArgParse_slides():
    parser = argparse.ArgumentParser(
        description="This script will automate the configuration process for a new switch"
    )

    parser.add_argument("--version", action="version", version="1.8")
    args = parser.parse_args()
    return args

def examfunc(A, B, target):
    try:
        product = A*B
        if product == target:
            return "Target Matched"
        else:
            return "Something went wrong"
    except:
        return "Something went wrong"



def main():
    with open("ExamFile.txt", "r") as file:
        for row in file: 
            if "I passed!" in row:
                print(row)  








if __name__ == "__main__":
    main()
