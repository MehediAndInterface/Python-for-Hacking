"""
Even or Odd: Ask for a number and print whether it is even or odd.
"""
number = input("Enter a number: ")

try:
    number_int = int(number)

    if number_int % 2 == 0:
        print(f"{number_int} is an even.")
    else:
        print(f"{number_int} is an odd.")

except ValueError:
    print("Invalid input. Please enter a whole number.")