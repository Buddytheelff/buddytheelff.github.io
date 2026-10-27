#!/usr/bin/env python

# Black formatter: shift + alt + F

import argparse
import pandas as pd
import plotly.express as px


def ArgParse_slides():
    parser = argparse.ArgumentParser(
        description="This script will create a line graph for the bean prices overtime "
    )
    parser.add_argument("--version", action="version", version="1.8")
    args = parser.parse_args()
    return args


def main():
    args = ArgParse_slides()
    # read CSV to pandas dataframe
    beans = pd.read_csv("beanSheet.csv")

    beans.columns = ["Time", "Bean Price"]
    # Creates the linechart
    lineChart = px.line(beans, x="Time", y="Bean Price")
    lineChart.show()


if __name__ == "__main__":
    main()
