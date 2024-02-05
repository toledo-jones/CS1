""" This is an interest calculating program designed to be used at the command line """
__author__ = "Cody Bogausch"
__version__ = "1.00"

def get_principle():
    principle = float(input("Enter your investment amount: "))
    if valid_input(principle):
        return principle

def get_years():
    years = int(input("Enter number of years: "))
    if valid_input(years, get_years):
        return years

def get_rate():
    interest_rate = float(input("Enter interest rate <as a decimal>: "))
    if valid_input(interest_rate, get_rate):
        return interest_rate


def calculate_interest(principle, years, rate):



def main():
    principle = get_principle()
    years = get_years()
    rate = get_rate()