#!/usr/bin/env python

import argparse, requests
import pandas as pd
from loguru import logger
from time import sleep
from datetime import datetime, timedelta

# file for log
logger.add("enchantment.log")


def ArgParse_slides():
    parser = argparse.ArgumentParser(
        description="This script will scrape the permits page for the core enchanments permit for the chosen month and provide a list of dates available"
        "It will notify via discord webhook a list of available dates"
    )
    parser.add_argument(
        "start_date",
        action="store",
        help="Enter the first day of the month you are planning on hiking in YYYY-MM-DD",
    )
    parser.add_argument(
        "timeToRun",
        action="store",
        help="Enter the number of days you would like this code to operate as an integer",
    )
    parser.add_argument("--version", action="version", version="2.0")
    args = parser.parse_args()
    return args


# from slides it takes my webhook and sends the message I give it
def discord_message(webhook, content):
    payload = {"content": content}
    response = requests.post(webhook, json=payload)

    if response.status_code == 204:
        logger.info("message sent to discord")
    else:
        logger.info("message unsuccessful")


def getterAvailablity(start_date):
    # Not entirely sure I need these but I don't want my code to get bot flagged
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/151.0.0.0 Safari/537.36"
        ),
        "Accept": "application/json",
    }

    # these are required for the API to send me information the extra 00s are for univeral time
    param = {
        "start_date": f"{start_date}T00:00:00.000Z",
        "commercial_acct": "false",
        "is_lottery": "false",
    }
    # gets the website availablity unfortunately in json
    r = requests.get(
        "https://www.recreation.gov/api/permits/233273/availability/month",
        params=param,
        headers=headers,
    ).json()

    # separate the .json I got from reservation.gov 30 is the identifier for the core enchantments permit
    jsonInfo = r["payload"]["availability"]["30"]["date_availability"]
    # https://www.geeksforgeeks.org/python/parsing-json-nested-dictionary-using-python/

    # Take that filtered json dictionary and put it into a pandas dataframe in order to search it
    # https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.from_dict.html
    data = pd.DataFrame.from_dict(jsonInfo, orient="index")
    # https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html
    # Below indexs the dataframe and it filters the values to exclude days with no availablity
    availableDatesDF = data[data["remaining"] > 0]
    return availableDatesDF


def main():
    args = ArgParse_slides()
    discord = "*********!!!!!!!!!!!!!!!!!!YOUR WEBHOOK HERE!!!!!!!!!!!!!**************"
    runtime = datetime.now() + timedelta(days=int(args.timeToRun))
    while datetime.now() < runtime:
        try:
            dates = getterAvailablity(args.start_date)
            logger.info("Website successfully obtained information")
            # can't use if dates: for true or false in a pandas dataframe
            if not dates.empty:
                # https://www.w3schools.com/python/pandas/ref_df_iterrows.asp
                message = f"🏔️ The Core Enchantment permit has available dates!\n\n"
                for date, row in dates.iterrows():
                    message += f"Date: {date[:10]}\n"
                    message += f"Total permits: {row["total"]}\nRemaining permits: {row["remaining"]}\n\n"

                discord_message(discord, message)
                logger.success("Success!")
            else:
                logger.info("No dates available")
        except:
            logger.critical("failure")
        sleep(43200)


if __name__ == "__main__":
    main()
