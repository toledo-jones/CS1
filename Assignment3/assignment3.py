"""
Write a Python application that calculates the amount of money earned on an investment.
 Prompt the user to enter an investment amount, the number of years for the investment,
  and the interest rate. Display an error message if the user enters 0 for any of these values;
   otherwise, display the total amount (balance) for each year of the investment. Save the file as assign3.py

Specific instructions:

    Program must use 4 (or more) functions to accomplish the following:
        Prompt for and return the investment amount (no arguments)
        Prompt for and return the number of years (no arguments)
        Prompt for and return the interest rate (no arguments)
        Display the calculations (3 arguments consisting of the values returned from the other functions)


    Your output must resemble the sample below. Notice the formatting of the dollar amounts.
     You need to display 2 decimal places for all amounts, even for those with whole dollar amounts.

"""
__author__ = "Cody Bogausch"
__version__ = "1.00"


def main() -> None:
    # Get user input for the investment
    principle = get_principle()
    years = get_years()
    rate = get_rate()

    # Print investment to console
    print_investment_balance_per_year(principle, years, rate)


def get_principle() -> float:
    """
    Prompt user for the principle amount of investment

    :return: Initial investment amount
    """

    # Keep prompting the user until we get a valid input
    while True:

        # Initial prompt
        principle = float(input("Enter your investment amount: "))

        # Principle must be larger than 0
        if principle > 0:

            # Input is valid, return early
            return principle

        # If we reach this point the input is invalid
        print("Invalid investment amount - please reenter")


def get_years() -> int:
    """
    Prompt user for the number of years

    :return: Number of years of investment
    """

    # Keep prompting the user until we get a valid input
    while True:

        # I honestly don't know how to do this without try and except blocks
        try:
            years = int(input("Enter the number of years: "))

            # Years must be above zero and an integer
            if years > 0:

                # Input is valid, return early
                return years

        # ValueError will be thrown if the user enters a non whole number
        except ValueError:
            pass

        # If we reach this point input is invalid
        print("Years must be a positive whole number - please reenter")


def get_rate() -> float:
    """
    Prompt user for interest rate

    :return: Interest rate between 0 and 1.
    """
    # Keep prompting the user until we get a valid input
    while True:

        # Initial prompt
        interest_rate = float(input("Enter interest rate <as a decimal>: "))

        # Interest rate must be between 0 and 1.
        if 0 < interest_rate < 1:

            # Input is valid, return early
            return interest_rate

        # If we reach this point the input is invalid
        print("Interest rate must be a positive decimal value - please reenter")


def print_investment_balance_per_year(
        principle: float,
        years: int,
        rate: float) -> None:
    """
    Iterate over each year that the investment collects interest.

    Print results to the console

    :param principle: Initial investment amount
    :param years: Number of years that the investment takes place
    :param rate: Interest rate per year
    """

    # Introduction, convert rate to percent
    print(f"Your investment at {rate * 100}% is: ")

    # Iterate over each year in the investment
    for year in range(years):
        # Calculate new principle
        principle = principle + principle * rate

        # Format decimals
        formatted_principle = "{:.2f}".format(principle)
        print(f"After year {year + 1}\t${formatted_principle}")


# Entry point
if __name__ == '__main__':
    main()
