""" This program asks for a a name and age"""

name = input("What is your name? ")
age = int(input("What is your age? "))

print(f"Your name is: {name}")
print(f"The number of letters in your name is: {len(name)}")
print(f"The first letter in your name is {name[0]}")
print(f"Your age is: {age}")
if age > 21:
    print("Congratulations you are old enough to drink alochol!")
else:
    print("Sorry, you are not old enough to drink alcohol.")