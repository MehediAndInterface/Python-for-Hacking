"""
Print a Triangle: Ask for a number and print a triangle of asterisks with that many rows.
"""

try:
    rows = int(input("Enter the number of rows for the triangle: "))

    # Check if the number is positive
    if rows > 0:
        # Loop from 1 to the number of rows (inclusive)
        for i in range(1, rows + 1):
            # On each line 'i', print 'i' asterisks
            print("*" * i)
    else:
        print("Please enter a positive number.")

except ValueError:
    print("Invalid input. Please enter a whole number.")