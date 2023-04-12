#import math


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


print("Welcome to the Simple Calculator!")
print("Please select an operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

while True:
    choice = input("Enter choice (1-4): ")
    try:
        choice = float(choice)
        break
    except ValueError:
        print("Follow the instructions you clown!")

while True:
    number_1 = input("Enter the first number: ")

    try:
        number_1 = float(number_1)
        break
    except ValueError:
        print("Hey this is no time for fun in games! Follow the instructions")

while True:
    number_2 = input("Enter the second number: ")

    try:
        number_2 = float(number_2)
        break
    except ValueError:
        print("Big bruh moment! Try AGAIN!")

while True:
    if choice in (1.0, 2.0, 3.0, 4.0):
        if choice == 1.0:
            print(number_1, "+", number_2, "=", add(number_1, number_2))

        elif choice == 2.0:
            print(number_1, "-", number_2, "=", subtract(number_1, number_2))

        elif choice == 3.0:
            print(number_1, "*", number_2, "=", multiply(number_1, number_2))

        elif choice == 4.0:
            print(number_1, "/", number_2, "=", divide(number_1, number_2))
        break
