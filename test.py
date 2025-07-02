"""
Print a Triangle: Ask for a number and print a triangle of asterisks with that many rows.
"""

try:
    rows = int(input("Enter a number: "))

    if rows > 0:
        for i in range(1, rows + 1):
            print("*" * i)
    else:
        print("Enter a positive number.")
except ValueError:
    print("Please enter a valid input")