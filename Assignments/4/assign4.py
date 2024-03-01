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
    """

    This program will collect user data, correct it for errors and display it in a nicely formatted, concise way.

    """

    names = get_name()

    initials = get_initials(names)

    phone_number = get_phone_number()

    display(names, initials, phone_number)


def display(
        names: list[str],
        initials: str,
        phone_number: str
) -> None:
    """
    Capitalize only the first letters of each part of the name, and print out the revised name.

    Print out the initials for that name.

    Print out the name in the format of:  Lastname, Firstname MI.  (for example:   Smith, John A.)

    Print out the phone number with parentheses, a space, and a dash. For example: (518) 828-4181.

    :param names: list of strings [first, middle, last] name, all lowercase.
    :param initials: first initial of first, middle and last name, capitalized.
    :param phone_number: string, ten-digit phone number
    :return: None
    """
    pass

    def get_full_name(_names: list[str]) -> str:
        """
        Convert from list of strings to properly formatted name

        :param _names: list of strings [first, middle, last] name, all lowercase.
        :return: string full name properly formatted
        """
        full_name = str()
        for name in names:
            full_name += name.capitalize() + " "

        return full_name.strip()

    print()
    print("You entered:", end=' ')
    print(get_full_name(names))

    print()
    print("Your initials are:", end=' ')
    print(initials)

    print()     # Trying to emulate your line spacing. Not entirely sure if every thing is spaced by one or two.
    print()     # I tried
    print("Displayed with last name first:", end=' ')
    print(f'{names[2].capitalize()}, {names[0].capitalize()} {names[1][0].capitalize()}.')

    print()
    print("Your phone number is:", end=' ')
    print(f'({phone_number[0:3]}) {phone_number[3:6]}-{phone_number[6:]}')


def get_name() -> list[str]:
    """
    Prompt the user to input their name

    :return: list of names [first, middle, last]
    """

    # Empty container for names
    names = list()

    # Repeatedly ask for name
    while len(names) != 3:

        # Spacer
        print()

        # Collect input and pass it to parse name
        names = parse_name(input("Enter your name as 'First Middle Last': "))

        # Handle incorrect input
        if len(names) != 3:
            print()
            print("Invalid Input")

    return names


def get_phone_number() -> str:
    """
    Prompts the user for their phone number and handles incorrect input accordingly

    :return: string containing a valid phone number
    """

    # Empty container for phone number
    phone_number = str()

    # TODO: Add support for international numbers
    def valid_phone_number(_phone_number: str) -> bool:
        """
        Nested function to check the validity of a phone number

        :param _phone_number: string containing a potentially valid phone number
        :return: bool if the phone number is a valid phone number
        """
        return len(_phone_number) == 10 and _phone_number.isnumeric()

    # Repeatedly ask for phone number
    while not valid_phone_number(phone_number):

        # Spacer
        print()

        # Collect user data
        phone_number = input("Enter 10 digit phone number <ex: 5158280021>: ")

        # Handle incorrect input
        if len(phone_number) > 10:
            print()
            print("Too many digits - please reenter")

        elif len(phone_number) < 10:
            print()
            print("Insufficient length - please reenter")
            # print("That's what she said")

        elif not phone_number.isnumeric():
            print()
            print("Phone number must be all digits - please reenter")

    return phone_number


def get_initials(names: list[str]) -> str:
    """
    Retrieve initials from a list of names [first, middle, last]
    :param names: list of names [first, middle, last]
    :return: string containing only the capitalized initials: "CPB"
    """

    # Container
    initials = str()

    # Iterate over names
    for name in names:

        # Add the first letter of each name to the initials container, capitalized
        initials += name[0].capitalize()

    return initials


def parse_name(name: str) -> list[str]:
    """
    Converts string of name with incorrect capitalization, leading and trailing white space to a
    list of all lower case names [first, middle, last]

    :param name: String containing the first middle and last name of the user
    :return: List of strings [first, middle, last]
    """

    # Remove excess whitespace around name ends a beginning
    name = name.strip()

    # Lowercase every character in the name string
    name = name.lower()

    # Split the name into a list of 3 containing the first middle and last
    names = name.split(" ")

    # Exit
    return names


if __name__ == '__main__':
    main()
