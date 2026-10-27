#!/usr/bin/env python

import argparse, csv
import matplotlib.pyplot as plt


def ArgParse_slides():
    parser = argparse.ArgumentParser(
        description="This script will plot a graph from a CSV "
    )
    parser.add_argument("--version", action="version", version="1.8")
    args = parser.parse_args()
    return args


def main():
    args = ArgParse_slides()

    try: 
        with open("cartheft.csv") as csvfile:
            reader = csv.reader(csvfile)
    except:
        print("No CSV file in directory!")
        quit()

    xaxis = []
    yaxis = []
    with open("cartheft.csv") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if row:
                xaxis.append(row[1])
                yaxis.append(
                    int(row[2])  # took me forever to find why it wouldn't start at 0
                )
    # get last ten values with negative indexing https://www.w3schools.com/python/gloss_python_string_negative_indexing.asp
    xaxis = xaxis[-10:]
    yaxis = yaxis[-10:]
    # sideways bar chart https://www.w3schools.com/python/matplotlib_bars.asp
    plt.barh(xaxis, yaxis, color="g")

    # labels
    plt.xlabel("Names of cars")
    plt.ylabel("# stolen")
    plt.title("I wish I had pandas")
    # make the graph
    plt.show()


if __name__ == "__main__":
    main()
