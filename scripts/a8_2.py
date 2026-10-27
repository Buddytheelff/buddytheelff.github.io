#!/usr/bin/env python

# Black formatter: shift + alt + F
"""Create a bar chart of the states and their population using a Pandas dataframe and Plotly:
- Hardcode the file statepop.csv, however you must first check that it exists."""

import argparse, csv
import pandas as pd
import plotly.express as px


def ArgParse_slides():
    parser = argparse.ArgumentParser(
        description="This script will use pandas and plotly to read a CSV and create a bar chart"
    )
    parser.add_argument("--version", action="version", version="1.9")
    args = parser.parse_args()
    return args


def main():
    args = ArgParse_slides()
    # check if file exists in directory
    try:
        with open("statepop.csv") as csvfile:
            reader = csv.reader(csvfile)
    except:
        print("No CSV file in directory!")
        quit()

    # read CSV to pandas dataframe
    states = pd.read_csv("statepop.csv")

    # add columns https://www.geeksforgeeks.org/pandas/add-column-names-to-dataframe-in-pandas/
    states.columns = ["State", "Population"]
    # Creates the barchart
    bChart = px.bar(states, x="State", y="Population")
    bChart.show()


if __name__ == "__main__":
    main()
