#!/usr/bin/env python

# Black formatter: shift + alt + F

import argparse, requests, csv
from bs4 import BeautifulSoup


def ArgParse_slides():
    parser = argparse.ArgumentParser(
        description="This script will vist the top 500 website, find the tr section where all the values are located"
        "Then it will grab the links and format these links into a list then write them to a csv"
    )
    parser.add_argument("--version", action="version", version="1.8")
    args = parser.parse_args()
    return args


def main():
    args = ArgParse_slides()
    # got these from burp suite!
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/151.0.0.0 Safari/537.36"
        )
    }

    soup = BeautifulSoup(
        requests.get("https://moz.com/top500", headers=headers).text, "html.parser"
    )
    domainls = []
    titleLs = []
    for tr in soup.find_all("tr"):
        link = tr.find_all(
            "a", href=True
        )  # I used .find() last time and that only grabbed the first itteration the .find_all() was the better choice
        if link:  # true or false testing if data exisits
            domainls.append(link[1]["href"])
            titleLs.append(link[1]["title"])

    domainls = domainls[:100]  # cuts the list down to first 100
    titleLs = titleLs[:100]  # again cuts the list down to 100

    # from your feedback I used the .zip() to combine these two lists and dict() to make them editable
    toCsv = dict(zip(domainls, titleLs))
    #checks domain for connection to show ERR for title if no connection works
    for domain in toCsv:
        try:
            requests.get(domain, headers=headers)
        except:
            toCsv[domain] = "ERR"
    # writes the list to the csv file
    with open("top100.csv", "w", newline="") as file:
        writer = csv.writer(file)
        for domain, title in toCsv.items():
            row = f"Title: {title}, Domain: {domain}"
            writer.writerow([row])
            # I ended up having to wrap the index with brackets cause it kept separating my string into multiple rows


if __name__ == "__main__":
    main()
