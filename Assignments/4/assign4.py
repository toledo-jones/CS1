#!/usr/bin/env python3

__author__ = "Cody Bogausch"
__version__ = "0.01a"

"""

    Write a Python program to do the following:
        Prompt for input of someone's first, middle, and last name as a single string (using any combination of upper 
        and lowercase letters). 
        Check to make sure the name was entered in the correct format (3 names separated by a single space). 
            If the input is not correct, continue to request the input again until the format is correct.
            If the user inputs any spaces in front of or behind the input string, ignore that white space
             and continue to process the input.
        Prompt for input of someone's phone number in 10 digit form (for example: 5188284181).
         If the input is not exactly 10 digits, continue to request the input again until the format is correct.
        
        Capitalize only the first letters of each part of the name, and print out the revised name.
        Print out the initials for that name.
        Print out the name in the format of:  Lastname, Firstname, MI.  (for example:   Smith, John A.)
        Print out the phone number with parentheses, a space, and a dash. For example: (518) 828-4181.

"""


def main() -> None:
    name = get_name()
    phone_number = get_phone_number()


def get_name() -> str:
    names = list()

    while len(names) != 3:
        print()
        name = input("Enter your name as 'First Middle Last': ")
        name = name.strip()
        names = name.split(" ")
        if len(names) != 3:
            print()
            print("Invalid Input")

    full_name = str()
    for name in names:
        name = name.lower()
        full_name += name.capitalize() + " "

    return full_name.strip()


def get_phone_number() -> str:
    phone_number = str()

    def valid_phone_number(_phone_number: str):
        return len(_phone_number) == 10 and _phone_number.isnumeric()

    while not valid_phone_number(phone_number):
        phone_number = input("Enter 10 digit phone number <ex: 5158280021>: ")

    return phone_number


def parse_name(name: str):
    pass


def display():
    pass


if __name__ == '__main__':
    main()
