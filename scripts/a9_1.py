#!/usr/bin/env python

import argparse, requests, re, csv
from time import strftime, sleep
from datetime import datetime, timedelta
from loguru import logger

# file for log
logger.add("beanPrice.log")

def ArgParse_slides():
    parser = argparse.ArgumentParser(
        description="This script will scrape the brofessors website and collect the price of beans with a while loop every 5 minutes."
        "write out the results to a file and using loguru to log"
    )
    parser.add_argument("--version", action="version", version="1.91")
    args = parser.parse_args()
    return args

def beanLog(
    beanPrice,
    time,
):
    # opens and appends to file
    pricels = [time, beanPrice[0]]
    with open("beanSheet.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(pricels)

def beanGetter(website):
    # gets value from website it seems this needs to run often to stop a bug
    r = requests.get(website)
    # groups the price between the stong tags and after the dollar sign for the csv file to create a chart
    beanPrice = re.findall(
        r"<\w+> \$(\d+\.\d+)<\/\w+>", r.text
    )  # https://docs.python.org/3/library/re.html#regular-expression-objects
    return beanPrice

def main():  # sorry about the nested while loops I couldn't think of a way to end at 30 minutes and check every 5 without them
    args = ArgParse_slides()
    endTime30 = datetime.now() + timedelta(minutes=30)# for the while loop to end

    # grabs the price the first time before the 30 minutes of 5 minutes wait
    try:
        time = strftime("%I:%M")  # 'I' is the normal hour clock
        beanPrice = beanGetter("https://the-security.ninja/beans")
        beanLog(beanPrice, time)  # only records price at start
        logger.success(
            f"Bean price acquired at {time}"
        )  # logs if bean price was get getted
    except:
        logger.critical(
            f"Failure to acquire price at {time}"
        )  # logs if the price was not aquired

    #start of 30 minute while loop
    while datetime.now() < endTime30:
        waitTime5 = datetime.now() + timedelta(minutes=5)
        while datetime.now() < waitTime5:  # it seems we need to access the site often
            logger.info(
                f"waiting 5 minutes in 20 second intervals current price: {beanPrice}"
            )
            beanPrice = beanGetter("https://the-security.ninja/beans")
            sleep(20)
        try:
            time = strftime("%I:%M")  # 'I' is the normal hour clock
            beanLog(beanPrice, time)  # only records price after 5 minutes

            logger.success(
                f"Bean price acquired at {time}"
            )  # logs if bean price was get getted
        except:
            logger.critical(
                f"Failure to acquire price at {time}"
            )  # logs if the price was not aquired

if __name__ == "__main__":
    try:  # wrapped main with a just in case
        main()
    except:
        print("not all gravy")
        logger.critical("Critical main() failure!")
