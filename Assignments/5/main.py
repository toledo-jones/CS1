#!/usr/bin/env python3
# coding: utf-8

"""
This module is a command line grading program

Evaluation and Grading
    Quizzes (20%)
    Projects (50%)
    Assignments (20%)
    Class Participation (10%)

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

Output will be exactly as follows:
------------------------------------------START----------------------------------------
CS 127 Grade Calculator

Description (?)

Enter name:
Enter the number of Assignments: 5

Enter grade for Assignment #1: 90
Enter grade for Assignment #2: 56
Enter grade for Assignment #3: 100
Enter grade for Assignment #4: 98
Enter grade for Assignment #5: 100

Enter the number of Quizzes: 6

Enter grade for Quiz #1: 90
Enter grade for Quiz #2: 56
Enter grade for Quiz #3: 100
Enter grade for Quiz #4: 98
Enter grade for Quiz #5: 100
Enter grade for Quiz #6: 100

Enter the number of Projects: 6

Enter grade for Project #1: 90
Enter grade for Project #2: 56
Enter grade for Project #3: 100
Enter grade for Project #4: 98
Enter grade for Project #5: 100
Enter grade for Project #6: 100

How many class sessions did you miss this semester? 2


Code/algorithm:
Average the quiz scores, then multiply by .20
Average the project scores, then multiply by .50
Average the assignment scores, then multiply by .20
Calculate participation grade (10%)
Total all the calculations above
Determine letter grade

Print report
------------------------------------------END------------------------------------------

 Functions:
    main
    header
    get_letter_grade
    enter_grades


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

    @return: String to be printed at the top of the program
    """
    return (
        '*********************************************\n'
        'CS 127 Grade Calculator\n'
        '*********************************************\n'
        'This program will accept user input and calculate a final grade\n'
        'for the semester.\n'
        '*********************************************\n'
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

    @param average: (float) final average grade
    @return: (str) letter grade representation
    """

    # I thought about this for a while and googled around and found:
    # https://stackoverflow.com/questions/39358092/range-as-dictionary-key-in-python/39358140#39358140

    # The fastest way to do this is apparently to subclass Dict and allow a range as a key like:
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


def enter_grades(
        number_of_entries: int,
        grade_type: str
) -> list:
    """
    Assign a grade to each entry of a single type of grade, i.e. quizzes, projects, etc

    @param number_of_entries: (int) number of entries for this type of assignment
    @param grade_type: (str) type of grade entry (quiz, project)
    @return:
    """

    # Use this to convert to a logical sentence in the command line
    grade_type_to_singular = {
        "Quizzes": "Quiz",
        "Projects": "Project",
        "Assignments": "Assignment"
    }

    # Empty container to store grades
    grades = list()

    # Iterate over each entry in the grade category
    for index in range(number_of_entries):

        grade = None

        def valid_input(_grade):
            return isinstance(grade, float) and 0 <= grade <= 100

        while not valid_input(grade):
            # Obtain user input
            try:
                grade = float(input(
                    f"Enter grade for {grade_type_to_singular[grade_type]} #{index + 1}: "
                ))
                if not valid_input(grade):
                    print("Enter a valid grade. ")

            except ValueError:
                print("Enter a valid grade:")


def get_user_grades(weights: dict) -> dict:
    """
    Use the command line to obtain valid inputs from the user for their grades

    @param weights: (dict){"Grade Type" : (float) weight}
    @return: ?!
    """
    for grade_type in weights:
        number_of_entries = None

        def valid_input(_number_of_entries: any) -> bool:
            """
            Determine validity of input for number of entries
            @param _number_of_entries: user inputted number of entries
            @return: (bool) if input is valid
            """
            return isinstance(_number_of_entries, int) and _number_of_entries > 0

        while not valid_input(number_of_entries):
            try:

                number_of_entries = int(input(
                    f"Enter the number of {grade_type}: "
                ))

                if not valid_input(number_of_entries):
                    print("Enter a valid number of entries.")

            except ValueError:
                print("Enter a valid number of grade entries.")

        grades = enter_grades(number_of_entries, grade_type)

        weights[grade_type] = grades


def main() -> None:
    """
    Entry point
    """

    # Print header at top of program
    print(header())

    # Weighted (percentage) of final grade
    weights = {
        'Quizzes': .2,
        'Projects': .5,
        'Assignments': .2,
        'Participation': .1
    }

    # Container to store grades
    grades = get_user_grades(weights)


# Executable boilerplate
if __name__ == '__main__':
    main()
