#!/usr/bin/env python
import argparse
from datetime import datetime, timedelta

def ArgParse_slides():
    parser = argparse.ArgumentParser(description="This script will help identify when bank balance goes below 1000. " \
    "It will also show predicted bank account balances weekly." \
    "It will keep track of debts and more features TBD")
    parser.add_argument("startCash",action='store', help="Enter the amount of cash in bank at the moment")
    parser.add_argument("lastPayday",action='store', help="Enter the last payday in YYYY-MM-DD")
    parser.add_argument("endDate",action='store', help="Enter the final date in YYYY-MM-DD")
    parser.add_argument("--version",action='version', version='1.0')
    args=parser.parse_args()
    return args

def main():
    args=ArgParse_slides()
    balance = float(args.startCash)
    current_date = datetime.now().date()
    endDate = datetime.strptime(args.endDate, "%Y-%m-%d").date()
    nextPay = datetime.strptime(args.lastPayday, "%Y-%m-%d").date()

    # Example numbers only. Replace with your own monthly bills and income.
    bills = {
        1: [1250, 65, 40],   # rent, internet, utilities
        5: 275,              # loan payment
        15: [120],           # insurance
        20: 100,             # recurring expense
        30: [60, 75]         # subscriptions and savings transfer
    }
    pay = 2000  # example biweekly take-home pay

    checkin = int(input("How many days between checks: "))# allows me to enter the number of days between balance check ins
    spendOpt = int(input("Large purchase? Enter 0 for no. Enter amount of purchase: "))
    checkDay = current_date #establish the checkday counter
    balance -= spendOpt
    while current_date <= endDate:
        if current_date == nextPay: # catches paydays and adds them to the balance 
            print(f"payday on {nextPay}. Your current balance is: {balance+pay}") #I wanted to have a quick check in on paydays
            balance += pay
            nextPay += timedelta(days=14)
        if current_date == checkDay:
            print(f"Your current balance on {checkDay} is: {balance}")
            checkDay = current_date + timedelta(days=checkin)

        #check for the bill days
        if current_date.day in bills:
            if type(bills[current_date.day]) == int:
                balance = balance - bills[current_date.day]
            else:
                for i in bills[current_date.day]: #i is the value assosiated with the key like a sample amount 
                    balance = balance - i
        if balance < 1000.0:
            print(f"Warning the balance fell below 1000 on {current_date}. Current balance {balance}")
        current_date += timedelta(days=1)


if __name__ == "__main__":
    main()