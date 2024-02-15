# !/usr/bin/env python3
# coding: utf-8

__author__ = "Cody Bogausch"
__version__ = "Pre-Alpha .01"

from math import pi

def main():
    print_initials()
    print_area_of_a_rectangle()
    print_area_of_a_triangle()
    print_area_of_a_circle()

def print_initials():
    """
    Prints initials in an ASCI style
    """
    print(r"     \           CCCCC   PPPPP    BBBB            /         ")
    print(r"      \\         C       P    P   B   B          //         ")
    print(r"=======>>        C       PPPPP    BBBB          <<=======   ")
    print(r"      //         C       P        B   B          \\         ")
    print(r"     /           CCCCC   P        BBBB            \         ")
    # Raw strings are so helpful for this.

def print_area_of_a_rectangle():
    """
    Takes user input for a the base and height of a rectangle and prints the area to the console
    """
    print("Area of a Rectangle:")
    width = float(input("Enter the width: "))
    height = float(input("Enter the height: "))
    area = width * height
    print_area(area)

def print_area_of_a_triangle():
    """
    Takes user input for the base and height of a triangle and prints the area to the console
    """
    print("Area of a Triangle:")
    width = float(input("Enter the width: "))
    height = float(input("Enter the height: "))
    area = (width * height) / 2
    print_area(area)

def print_area_of_a_circle():
    """
    Takes user input for a radius and prints the area to the console
    """
    print("Area of a Circle:")
    radius = float(input("Enter the radius: "))
    area = pi * radius ** 2
    print_area(area)

def print_area(area):
    print(f"Area is equal to {area}")

if __name__ == '__main__':
    main()