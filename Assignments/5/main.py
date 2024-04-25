#!/usr/bin/env python3
# coding: utf-8

"""
########################################################################################################################

    This module is a command line grading program
    Assignment 5 for CS127
    It is written in a functional style, rather than an object-oriented one.

########################################################################################################################

Output will be modeled after the following:
----------------------------------START----------------------------------------
CS 127 Grade Calculator
Description (?)
Enter name:
Enter the number of Assignments: 1
Enter grade for Assignment #1: 90
Enter the number of Quizzes: 1
Enter grade for Quiz #1: 90
Enter the number of Projects: 1
Enter grade for Project #1: 90
How many class sessions did you miss this semester? 2
Average the quiz scores, then multiply by .20
Average the project scores, then multiply by .50
Average the assignment scores, then multiply by .20
Calculate participation grade (10%)
Total all the calculations above
Determine letter grade
Print report (name, averages for categories, total average, letter grade)
Write record to a file
Prompt for additional students (y/n) – repeat if necessary
(don’t ask for # of quizzes, projects, assignments again)
-------------------------------------END----------------------------------------

 Functions:
    main
    format_final_grades
    get_final_grade
    get_grade_categories
    get_grade_entries
    get_letter_grade
    get_valid_input
    header
    write_final_grades


 ChangeLog:    Cody Bogausch
           (cody.bogausch@sunycgcc.edu)


 Version 1.0
   April 23, 2024

"""

__author__ = "Cody Bogausch"
__version__ = "1.0"


def header() -> str:
    """
    Modifiable header

    :return: (str) to be printed at the top of the program
    """
    return (
        '***************************************************************************************************\n'
        'CS 127 Grade Calculator\n'
        '***************************************************************************************************\n'
        'This program will accept user input and calculate a final grade\n'
        'for the semester.\n'
        '***************************************************************************************************\n'
    )


def get_letter_grade(average: float) -> str:
    """
    Convert a weighted average to a letter grade

    Grading Scale:
        A 93 – 100

        A- 90 – 92

        B+ 87 – 89

        B 83 – 86

        B- 80 – 82

        C+ 77 – 79

        C 73 – 76

        C- 70 – 72

        D 65 – 69

        F Below 65

    :param average: (float) final average grade
    :return: (str) letter grade representation
    """

    # I thought about this for a while and googled around and found:
    # https://stackoverflow.com/questions/39358092/range-as-dictionary-key-in-python/39358140#39358140

    # The fastest way to do this is apparently to subclass Dict and allow a range as a key with a custom class,
    # giving us the ability to do:
    # {range(0, 65): "F", etc}

    # I think this way is fine and very readable, albeit a bit simple
    if average < 65:
        return "F"
    elif average <= 69:
        return "D"
    elif average <= 72:
        return "C-"
    elif average <= 76:
        return "C"
    elif average <= 79:
        return "C+"
    elif average <= 82:
        return "B-"
    elif average <= 86:
        return "B"
    elif average <= 89:
        return "B+"
    elif average <= 92:
        return "A-"
    elif average <= 100:
        return "A"


def get_final_grade(grades: dict) -> tuple:
    """
    Calculate the final grade based on weighted categories and return the average and letter grade and totals

    :param grades: (dict) grade categories as keys and tuples with weight and list of grades as values.
    :return: (tuple) the weighted average, letter grade, and a dictionary with weighted scores for each category.
    """
    # Create a copy of the grades dictionary to store weighted scores
    totals = dict(grades)

    # Iterate over grade categories
    for grade_category, (weight, items) in grades.items():
        match grade_category:
            case "Participation":
                # Calculate weighted absences and bound them between 0 and 5
                weighted_absences = min(max(items - 3, 0), 5)

                # Incorporate the absences into the weight
                weighted_average = (100 - 20 * weighted_absences) * weight

                # Store the weighted average for the category
                totals[grade_category] = weighted_average
            case _:
                # Calculate the weighted average for other categories

                number_of_grades = len(items)
                combined_grades = sum(items)
                totals[grade_category] = ((combined_grades / number_of_grades) * weight)

    # Calculate the overall average by summing the weighted scores
    average = sum(totals.values())

    # Convert the average to a letter grade
    letter_grade = get_letter_grade(average)

    # Return the average, letter grade, and weighted scores for each category
    return average, letter_grade, totals


def get_valid_input(
        prompt: str,
        input_type: type,
        validation_function=None
) -> any:
    """
    Obtain valid input from the user with arbitrary prompt, validation and input type

    :param prompt: (str) prompt to display to the user
    :param input_type: (type) expected data type of the input
    :param validation_function: (function) optional validation function to check input validity
    :return: (any) valid input from the user
    """

    # Loop until valid input is obtained
    while True:
        # Display prompt and wait for user input
        user_input = input(prompt)
        try:
            # Convert user input to the specified type
            user_input = input_type(user_input)

            # Check if validation function exists and if the input passes validation
            if validation_function is None or validation_function(user_input):
                # Return valid input
                return user_input
            else:
                # If input fails validation, prompt user to try again
                print("Invalid input. Please try again.")

        # Handle ValueError if conversion to specified type fails
        except ValueError:

            # Prompt user to try again if conversion fails
            print("Invalid input. Please try again.")


def get_grade_entries(
        number_of_entries: int,
        grade_category: str
) -> list:
    """
    Assign a grade to each entry of a single type of grade, i.e. quizzes, projects, etc

    :param number_of_entries: (int) number of entries for this type of assignment
    :param grade_category: (str) type of grade entry (quiz, project)
    :return: (list) List of grades
    """
    grade_type_to_singular = {
        "Quizzes": "Quiz",
        "Projects": "Project",
        "Assignments": "Assignment"
    }
    grades = []

    # Iterate over each item in the the number of entries for this grade category
    for index in range(number_of_entries):
        # Collect grade
        grade = get_valid_input(
                f"Enter grade for {grade_type_to_singular[grade_category]} #{index + 1}: ",
                float,
                lambda x: 0 <= x <= 100
        )

        # Add entry to the list of grades for this category
        grades.append(grade)

    # Branch of to remove the lowest quiz. Make sure not to remove the only one
    if grade_category == 'Quizzes' and len(grades) > 1:
        # Remove the lowest grade
        grades.remove(min(grades))

    # Return list of grades for this category
    return grades


def get_grade_categories(
        weights: dict,
        determine_entries: bool
) -> dict:
    """
    Use the command line to obtain valid inputs from the user for their grades

    :param determine_entries:
    :param weights: (dict) {"Grade Type" : (float) weight}
    :return: (dict) Dictionary containing grade categories and their weights
    """
    for grade_category, (weight, grades) in weights.items():
        match grade_category:
            case "Participation":
                # Collect number of absences
                absences = get_valid_input(
                        "How many classes did you miss this semester? ",
                        int,
                        lambda x: x >= 0
                )

                # Add to dictionary of grade of weights, category: [weight, [grades]]
                weights[grade_category] = [weight, absences]

            case _:
                # This branch breaks off to change the program structure when it is entering a second students grades
                if determine_entries:
                    # Collect the number of grades from the user
                    number_of_entries = get_valid_input(
                            f"Enter the number of {grade_category}: ",
                            int,
                            lambda x: x > 0
                    )
                else:
                    # The number of grades is already known, obtain it from the weights: category: [weights, [grades]]
                    #                                                                                       ^ length of
                    number_of_entries = len(weights[grade_category][1])

                # Obtain a value for each entry in the category
                grades = get_grade_entries(number_of_entries, grade_category)

                # Add to dictionary of grade of weights, category: [weight, [grades]]
                weights[grade_category] = [weight, grades]

    # Return dictionary of grade weights with accurately filled in data
    return weights


def format_final_grades(
        name: str,
        average: float,
        letter_grade: str,
        totals: dict
) -> str:
    """
    Format and return final grades in a readable, single string

    :param name: (str) name inputted by the user.
    :param average: (float) final calculated average
    :param letter_grade: (str) final calculated letter grade
    :param totals: (dict) averages for each grade category
    :return: (str) formatted string to be printed and written as output to a file
    """

    # Non algorithmic formatting:
    output = (
        f"\n"
        f"\n"
        f"##################################################################\n"
        f"***************************FINAL GRADES:**************************\n"
        f"##################################################################\n"
        "\n"
        f"\t----------------------------------------\n"
        f"\t\t{name}\n"
        f"\t----------------------------------------\n"
        f"\tYour final average is:\t {average}%\n"
        f"\tYour letter grade is:\t {letter_grade}\n"
        f"\t----------------------------------------\n"
    )

    # More complex formatting for the data stored in the dictionary
    for grade_category, average in totals.items():
        # Iterate over each category and add its value to the output string
        output += f"\t{grade_category} : {average}%\n"

    # Endpoint for clarity
    output += f"\t----------------------------------------\n"

    # Return formatted string as one variable
    return output


def write_final_grades(formatted_output: str) -> None:
    """
    Write grader output to file

    :param formatted_output: (str) output collected from the user and formatted properly
    :return: None
    """
    # Open output.txt as write
    with open("output.txt", "w") as file:
        # Write formatted output to file
        file.write(formatted_output)


def main(
        determine_number_of_entries: bool = True,
        weights=None
) -> None:
    """
    Requirements:

    - Must utilize functions

    - Name can't be blank, format: First Last

    - assignments can't be blank, must be > 0, must be int

    - individual grades for assignments and projects must be int and > 0

    - individual grades for quizzes must be float and > 0

    - drop the lowest quiz grade
    :param determine_number_of_entries: (bool) if the user should specify the number of grade entries in a category
    :param weights: (dict) pre-existing data structure to store data about the grades, categories and weights
    :return: None
    """

    # First time running this will be true, otherwise it is set to False
    if determine_number_of_entries:
        # Print header at top of program
        print("\n" + header())

    # Collect name
    name = get_valid_input(
            f"Enter your name (First Last): ",
            str,
            lambda x: len(x.split()) == 2
    )

    # Weights are at their default so assign the structure:
    if weights is None:
        # Weighted (percentage) of final grade
        weights = {
            'Quizzes': [.2, list()],
            'Projects': [.5, list()],
            'Assignments': [.2, list()],
            'Participation': [.1, list()]
        }

    # Container to store grades
    grades = get_grade_categories(
            weights,
            determine_number_of_entries
    )

    # Calculate final grade
    average, letter_grade, totals = get_final_grade(grades)

    # Format and determine output
    formatted_output = format_final_grades(
            name,
            average,
            letter_grade,
            totals
    )

    # Print output formatted above
    print(formatted_output)

    # Write to file
    write_final_grades(formatted_output)

    # Repeat if necessary:
    repeat = get_valid_input(
            f"Would you like to enter a grade for another student? (Y/N): ",
            str,
            lambda x: x.upper() == "Y" or x.upper() == "N"
    )

    # If the user answered yes
    if repeat.upper() == "Y":
        # Recurse, changing the default weights and do not collect the number of entries in a category again
        main(
                determine_number_of_entries=False,
                weights=grades
        )

    # Exit
    if letter_grade == "F":
        # Better luck next time! Loser!
        print(f"See you next year, {name}!")
    else:
        # Thanks for coming to my TED talk
        print("Mr. Scampoli says \'Have a great summer!\'")


# Executable boilerplate
if __name__ == '__main__':
    main()
